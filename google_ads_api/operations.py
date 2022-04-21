def create_pause_campaign(customer_id:str, campaign_id:str):
    """Create an operation to pause a campaign"""
    return {
        'updateMask': 'status',
        'update': {
            'resourceName': f'customers/{customer_id}/campaigns/{campaign_id}',
            'status': 'PAUSED'
        }
    }


def create_enable_campaign(customer_id:str, campaign_id:str):
    """Create an operation to enabled a campaign"""
    return {
        'updateMask': 'status',
        'update': {
            'resourceName': f'customers/{customer_id}/campaigns/{campaign_id}',
            'status': 'ENABLED'
        }
    }


def create_update_budget(customer_id:str, budget_id:str, amount: str):
    """Create an operation to update a campaign budget"""
    return {
        'updateMask': 'amount_micros',
        'update': {
            'resourceName': f'customers/{customer_id}/campaignBudgets/{budget_id}',
            'amount_micros': amount
        }
        
    }
