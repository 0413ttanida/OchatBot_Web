import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
import os

# スクリプトのディレクトリを基準にパスを解決
script_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(script_dir, "config.yaml")

# ユーザー設定読み込み
with open(yaml_path, 'r') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    cookie_key=config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days'],
)

# UI
authenticator.login()
if st.session_state["authentication_status"]:
    # ログイン成功
    st.write('# ログインしました!')
    st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout('Logout')

elif st.session_state["authentication_status"] is False:
    # ログイン成功ログイン失敗
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    # デフォルト
    st.warning('Please enter your username and password')
