import allure
import time
import pytest

from tests import client

@pytest.fixture(scope="function", autouse=True)
def story_account_register_account():
    allure.dynamic.story("Account queries accounts")
    allure.dynamic.label("permission", "no_permission_required")

@allure.label("sdk_test_id", "query_all_accounts")
def test_query_all_accounts():
    with allure.step('WHEN client queries all accounts'):
        all_accounts = client.query_all_accounts()
    with allure.step('THEN there should be some accounts present'):
        assert len(all_accounts) > 0, "No accounts found in the system"


@allure.label("sdk_test_id", "query_all_accounts_in_domain")
def test_query_all_accounts_in_domain(
        GIVEN_registered_domain_with_registered_accounts):
    with allure.step(
            f'WHEN client queries all accounts in domain "{GIVEN_registered_domain_with_registered_accounts}"'):
        time.sleep(3)
        accounts_in_domain = client.query_all_accounts_in_domain(GIVEN_registered_domain_with_registered_accounts)
    with allure.step(
            f'THEN the response should be a non-empty list of accounts in domain "{GIVEN_registered_domain_with_registered_accounts}"'):
        assert isinstance(accounts_in_domain, list) and accounts_in_domain, \
            f"Expected a non-empty list of accounts in the domain {GIVEN_registered_domain_with_registered_accounts}, got {accounts_in_domain}"

    