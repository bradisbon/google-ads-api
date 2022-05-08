import os


def load_env_var(key:str, default: str = None) -> str:
    env_var = os.getenv(key, default)

    if env_var is None:
        raise RuntimeError(f'google-ads-api: Required environment variable not set: {key}')

    return env_var


API_VERSION = load_env_var('GOOGLE_ADS_API_VERSION',)
MCC_ID = load_env_var('GOOGLE_ADS_MCC_ID')
CREDENTIALS_PATH = load_env_var('GOOGLE_ADS_CREDENTIALS_PATH','~/.credentials/googleads.yaml')
