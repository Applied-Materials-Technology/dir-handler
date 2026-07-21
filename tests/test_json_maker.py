import pytest
import json
import dirhandler as dh

### TEST START UP

def test_start_and_create_structure(tmp_path, monkeypatch, capsys):

    # Test if the start function correctly creates test folder

    monkeypatch.chdir(tmp_path)
    json_file = tmp_path / "structure.json"
    json_file.write_text(json.dumps({"project": {"data": {}}}))

    dh.start(str(json_file), example=False, testing=True)
    assert (tmp_path / "testpath" / "my_generated_project" / "project" / "data").is_dir()
    captured = capsys.readouterr()
    assert "Generating folder structure in:" in captured.out

def test_start_loads_example_file(monkeypatch, tmp_path):

    # Test if the start function loads the example json when running example=True

    monkeypatch.chdir(tmp_path)
    example_path = tmp_path / "src" / "dirhandler" / "examples"
    example_path.mkdir(parents=True)
    (example_path / "sample.json").write_text(json.dumps({"x": {}}))

    dh.start("sample.json", example=True, testing=True)
    assert (tmp_path / "testpath" / "my_generated_project" / "x").is_dir()


### TEST CREATE STRUCTURE

def test_create_structure_dict(tmp_path):

    # Test if simple dictionary creates the correct folder structure

    structure = {"project": {"data": {}, "logs": {}}}
    dh.create_structure(tmp_path, structure, {})
    assert (tmp_path / "project").is_dir()
    assert (tmp_path / "project" / "data").is_dir()
    assert (tmp_path / "project" / "logs").is_dir()

def test_create_structure_list_and_placeholder(tmp_path):

    # Test if translations are correctly applies to dictionary structure

    structure = ["run[2]", {"config": ["env[test]"]}]
    translations = {"test": ["dev", "prod"]}
    dh.create_structure(tmp_path, structure, translations)
    assert (tmp_path / "run1").is_dir()
    assert (tmp_path / "run2").is_dir()
    assert (tmp_path / "config" / "envdev").is_dir()
    assert (tmp_path / "config" / "envprod").is_dir()

### TEST PARSE PLACEHOLDER

def test_parse_placeholder_plain():

    # Test plain keys without placeholder syntax should return the original key

    assert dh.parse_placeholder("data", {}) == ["data"]

def test_parse_placeholder_numeric():

    # Test numeric placeholders should expand to sequential numbered names

    assert dh.parse_placeholder("run[3]", {}) == ["run1", "run2", "run3"]

def test_parse_placeholder_named_translation():

    # Test named placeholders should expand using the provided translations mapping

    translations = {"env": ["dev", "prod"]}
    assert dh.parse_placeholder("service[env]", translations) == ["servicedev", "serviceprod"]

def test_parse_placeholder_missing_translation():

    # missing translation keys should raise KeyError

    with pytest.raises(KeyError):
        dh.parse_placeholder("service[missing]", {})


### TEST EDGE CASES

def test_create_structure_empty_values(tmp_path):

    # Test if empty lists and dictionaries still create the corresponding folders

    structure = {"project": [], "empty": {}}
    dh.create_structure(tmp_path, structure, {})
    assert (tmp_path / "project").is_dir()
    assert (tmp_path / "empty").is_dir()

def test_create_structure_empty_list(tmp_path):

    # Test if an empty list still creates the corresponding folder

    structure = ["folder", []]
    dh.create_structure(tmp_path, structure, {})
    assert (tmp_path / "folder").is_dir()

def test_start_invalid_file_raises_file_not_found(monkeypatch, tmp_path):

    # Test if the start function raises FileNotFoundError for a missing JSON file

    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        dh.start("missing.json", example=False, testing=True)