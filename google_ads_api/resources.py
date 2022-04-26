import json
import typing

from google_ads_api import constants

import aiohttp


async def customers_search(session: aiohttp.ClientSession,
                     customer_id: str,
                     query: str):
    """Query the Customer resource"""

    data = {
        'pageSize': 10000,  # page size defaults to 10,000 if not set here
        'query': query,
    }

    response = await session.post(f'https://googleads.googleapis.com/{constants.API_VERSION}/customers/{customer_id}/googleAds:search',
                        data=json.dumps(data))
    response.raise_for_status()

    return await response.json()


async def campaigns_mutate(session: aiohttp.ClientSession,
                           customer_id: str,
                           operations: typing.List):
    """Mutate campaigns"""

    data = {'operations':operations,
            'responseContentType': 'MUTABLE_RESOURCE'}

    response = await session.post(f'https://googleads.googleapis.com/{constants.API_VERSION}/customers/{customer_id}/campaigns:mutate',
                                  data=json.dumps(data))
    if not response.ok:
        print(await response.text())
    response.raise_for_status()

    return await response.json()


async def campaign_budgets_mutate(session: aiohttp.ClientSession,
                           customer_id: str,
                           operations: typing.List):
    """Mutate campaign budgets"""

    data = {'operations':operations,
            'responseContentType': 'MUTABLE_RESOURCE'}

    response = await session.post(f'https://googleads.googleapis.com/{constants.API_VERSION}/customers/{customer_id}/campaignBudgets:mutate',
                                  data=json.dumps(data))
    response.raise_for_status()

    return await response.json()


async def list_customers(session: aiohttp.ClientSession) -> typing.Dict[str,str]:
    """Fetch a dict of customers and ids"""

    response = await customers_search(session, constants.MCC_ID, "SELECT customer_client.id, customer_client.descriptive_name FROM customer_client WHERE customer_client.status = 'ENABLED'")
    return {c['customerClient']['descriptiveName']:c['customerClient']['id'] for c in response['results']}

