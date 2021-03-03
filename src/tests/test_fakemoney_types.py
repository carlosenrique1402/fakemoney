import unittest
import uuid
from datetime import date
import fakemoney.types


class TestFakeMoneyTypes(unittest.TestCase):
    def test_email_invalid_email(self):
        valid = fakemoney.types.email.validate("this is not an email")
        assert valid == False

    def test_email_valid_email_subdomain(self):
        valid = fakemoney.types.email.validate("info@fakemoney.ekiim.xyz")
        assert valid == True

    def test_email_valid_email(self):
        valid = fakemoney.types.email.validate("info@ekiim.xyz")
        assert valid == True

    def test_phone_invalid_not_a_number(self):
        valid = fakemoney.types.phone.validate("not a phone number")
        assert valid == False

    def test_phone_invalid_number(self):
        valid = fakemoney.types.phone.validate("123456789")
        assert valid == False

    def test_phone_valid_number_mx(self):
        valid = fakemoney.types.phone.validate("+526641234567")
        assert valid

    def test_phone_valid_number_us(self):
        valid = fakemoney.types.phone.validate("+16199123456")
        assert valid

    def test_md5_invalid_not_md5(self):
        valid = fakemoney.types.md5.validate("notAhash")
        assert valid == False

    def test_md5_valid_trim_md5(self):
        valid = fakemoney.types.md5.validate("f4adf8577e27e12b70753bb04cd")
        assert valid == False

    def test_md5_valid(self):
        valid = fakemoney.types.md5.validate("10297f4adf8577e27e12b70753bb04cd")
        assert valid

    def test_url_invalid_scheme(self):
        valid = fakemoney.types.url.validate("ftp://ekiim.xyz/")
        assert valid == False

    def test_url_valid_scheme_http(self):
        valid = fakemoney.types.url.validate("http://ekiim.xyz/")
        assert valid

    def test_url_valid_scheme_https(self):
        valid = fakemoney.types.url.validate("https://ekiim.xyz/")
        assert valid

    def test_birthdate_valid(self):
        _date = date(1994,12,23)
        valid = fakemoney.types.birthdate.validate(_date)
        assert valid

    def test_birthdate_invalid(self):
        _date = "1994/12/23"
        valid = fakemoney.types.birthdate.validate(_date)
        assert valid == False

    def test_str_nonempty_valid(self):
        _str = "Test"
        valid = fakemoney.types.str_nonempty.validate(_str)
        assert valid

    def test_str_nonempty_valid_spaces(self):
        _str = "   "
        valid = fakemoney.types.str_nonempty.validate(_str)
        assert valid == False

    def test_str_nonempty_invalid_by_len(self):
        _str = ""
        valid = fakemoney.types.str_nonempty.validate(_str)
        assert valid == False

    def test_str_nonempty_invalid_by_type(self):
        _str = None
        valid = fakemoney.types.str_nonempty.validate(_str)
        assert valid == False

    def test_list_of_builtin_str_valid(self):
        _type = fakemoney.types.list_of(str)
        assert _type.validate(["hello"]) == True

    def test_list_of_builtin_str_valid_multiple(self):
        _type = fakemoney.types.list_of(str)
        assert _type.validate(["hello", "world"]) == True

    def test_list_of_builtin_str_invalid(self):
        _type = fakemoney.types.list_of(str)
        assert _type.validate([1]) == False

    def test_list_of_builtin_str_invalid_multiple_at_start(self):
        _type = fakemoney.types.list_of(str)
        assert _type.validate([1, "hello"]) == False

    def test_list_of_builtin_str_invalid_multiple_not_at_start(self):
        _type = fakemoney.types.list_of(str)
        assert _type.validate(["hello", 1]) == False

    def test_list_of_custom_email_valid(self):
        _type = fakemoney.types.list_of(fakemoney.types.email)
        assert _type.validate(["info@ekiim.xyz"]) == True

    def test_list_of_custom_email_invalid(self):
        _type = fakemoney.types.list_of(fakemoney.types.email)
        assert _type.validate(["not-an-email"]) == False


    def test_uuid_create_full(self):
        _path = 'path'
        timestamp = 1614397097.4951427
        _collection = 'default'
        _uuid = fakemoney.types.UUID.create(
            'path',
            timestamp=timestamp,
            _collection=_collection
        )
        assert isinstance(_uuid, uuid.UUID)

    def test_uuid_create_no_collection(self):
        _path = 'path'
        timestamp = 1614397097.4951427
        _uuid = fakemoney.types.UUID.create(
            'path',
            timestamp=timestamp,
        )
        assert isinstance(_uuid, uuid.UUID)

    def test_uuid_create_no_time(self):
        _path = 'path'
        _collection = 'default'
        _uuid = fakemoney.types.UUID.create(
            'path',
            _collection=_collection
        )
        assert isinstance(_uuid, uuid.UUID)

    def test_uuid_validate_valid(self):
        _uuid = uuid.uuid4()
        assert fakemoney.types.UUID.validate(_uuid) == True

    def test_uuid_validate_invalid(self):
        _uuid = "not-a-uuid"
        assert fakemoney.types.UUID.validate(_uuid) == False
