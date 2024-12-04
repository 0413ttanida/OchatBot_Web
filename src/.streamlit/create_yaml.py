import yaml
from yaml.loader import SafeLoader

import streamlit as st
import streamlit_authenticator as stauth

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
yaml_data = stauth.Hasher.hash_passwords(config['credentials'])

with open('../config.yaml', "w") as f:
    yaml.dump(yaml_data, f)
    print("完了")
