import pytest

from app import config, validators


@pytest.fixture(scope="module", autouse=True)
def setup_teardown(*args, **kwargs):
    config.ALLOWED_CHANNELS.append('test_channel')
    config.ALLOWED_DOMAINS.append('test_company')

    yield

    config.ALLOWED_CHANNELS.remove('test_channel')
    config.ALLOWED_DOMAINS.remove('test_company')


def test_validate_return_error_with_invalid_domains():
    invalid_domain_payload = {
        'team_domain': 'invalid',
    }
    invalid_channel_payload = {
        'team_domain': 'test_company',
        'channel_name': 'invalid'
    }
    invalid_text_payload = {
        'team_domain': 'test_company',
        'channel_name': 'test_channel',
        'text': 'Invalid'
    }

    payloads = [
        (invalid_domain_payload, "Your domain invalid is not allowed to use this command"),
        (invalid_channel_payload, "The channel invalid is not allowed to use this command"),
        (invalid_text_payload, "You need to provide a pull request link"),
    ]

    for payload, expected_error in payloads:
        _, error = validators.validate(payload)
        assert error == expected_error


def test_validate_return_data_with_correct_payload():
    payload = {
        'team_domain': 'test_company',
        'channel_id': 'UX12312',
        'channel_name': 'test_channel',
        'user_id': 'UXASD1231',
        'text': '<http://github.com/lucasmagnum/slack-reviewers/pull/01>'
    }

    data, error = validators.validate(payload)
    assert data == {
        'text': payload['text'],
        'user': payload['user_id'],
        'channel': payload['channel_id']
    }
    assert error is None
