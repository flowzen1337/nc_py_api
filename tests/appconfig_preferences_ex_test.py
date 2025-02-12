import pytest
from gfixture import NC_APP

from nc_py_api import NextcloudExceptionNotFound

if NC_APP is None or "app_ecosystem_v2" not in NC_APP.capabilities:
    pytest.skip("app_ecosystem_v2 is not installed.", allow_module_level=True)


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_get_value_invalid(class_to_test):
    with pytest.raises(ValueError):
        class_to_test.get_value("")


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_get_values_invalid(class_to_test):
    assert class_to_test.get_values([]) == []
    with pytest.raises(ValueError):
        class_to_test.get_values([""])
    with pytest.raises(ValueError):
        class_to_test.get_values(["", "k"])


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_set_empty_key(class_to_test):
    with pytest.raises(ValueError):
        class_to_test.set("", "some value")


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_delete_invalid(class_to_test):
    class_to_test.delete([])
    with pytest.raises(ValueError):
        class_to_test.delete([""])
    with pytest.raises(ValueError):
        class_to_test.delete(["", "k"])


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_get_default(class_to_test):
    assert class_to_test.get_value("non_existing_key", default="alice") == "alice"


@pytest.mark.parametrize("value", ("0", "1", "12 3", ""))
@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_set_delete(value, class_to_test):
    class_to_test.delete("test_key")
    assert class_to_test.get_value("test_key") is None
    class_to_test.set("test_key", value)
    assert class_to_test.get_value("test_key") == value
    class_to_test.set("test_key", "zzz")
    assert class_to_test.get_value("test_key") == "zzz"
    class_to_test.delete("test_key")
    assert class_to_test.get_value("test_key") is None


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_delete(class_to_test):
    class_to_test.set("test_key", "123")
    assert class_to_test.get_value("test_key")
    class_to_test.delete("test_key")
    assert class_to_test.get_value("test_key") is None
    class_to_test.delete("test_key")
    class_to_test.delete(["test_key"])
    with pytest.raises(NextcloudExceptionNotFound):
        class_to_test.delete("test_key", not_fail=False)
    with pytest.raises(NextcloudExceptionNotFound):
        class_to_test.delete(["test_key"], not_fail=False)


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_get(class_to_test):
    class_to_test.delete(["test key", "test key2"])
    assert len(class_to_test.get_values(["test key", "test key2"])) == 0
    class_to_test.set("test key", "123")
    assert len(class_to_test.get_values(["test key", "test key2"])) == 1
    class_to_test.set("test key2", "123")
    assert len(class_to_test.get_values(["test key", "test key2"])) == 2


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_multiply_delete(class_to_test):
    class_to_test.set("test_key", "123")
    class_to_test.set("test_key2", "123")
    assert len(class_to_test.get_values(["test_key", "test_key2"])) == 2
    class_to_test.delete(["test_key", "test_key2"])
    assert len(class_to_test.get_values(["test_key", "test_key2"])) == 0
    class_to_test.delete(["test_key", "test_key2"])
    class_to_test.set("test_key", "123")
    assert len(class_to_test.get_values(["test_key", "test_key2"])) == 1
    class_to_test.delete(["test_key", "test_key2"])
    assert len(class_to_test.get_values(["test_key", "test_key2"])) == 0


@pytest.mark.parametrize("key", ("k", "k y", " "))
@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_get_non_existing(key, class_to_test):
    class_to_test.delete(key)
    assert class_to_test.get_value(key) is None
    assert class_to_test.get_values([key]) == []
    assert len(class_to_test.get_values([key, "non_existing_key"])) == 0


@pytest.mark.parametrize("class_to_test", (NC_APP.appconfig_ex_api, NC_APP.preferences_ex_api))
def test_cfg_ex_get_typing(class_to_test):
    class_to_test.set("test key", "123")
    class_to_test.set("test key2", "321")
    r = class_to_test.get_values(["test key", "test key2"])
    assert isinstance(r, list)
    assert r[0]["configkey"] == "test key"
    assert r[1]["configkey"] == "test key2"
    assert r[0]["configvalue"] == "123"
    assert r[1]["configvalue"] == "321"
