from fastapi import APIRouter, HTTPException
from typing import List, Dict, Optional, Annotated

from schema import schemas
from config.database import accounts_collection

from model.accounts import AccountModel


accountRouter = APIRouter()


# Create a new account
@accountRouter.post("/accounts", response_model= schemas.Account)
async def create_account(account: schemas.Account):
    AccountModel.createAccount(account)
    


# Get all accounts
@accountRouter.get("/accounts", response_model=List[schemas.Account])
async def get_all_accounts():
    accounts = AccountModel.getAccounts()
    return accounts

# Get an account by username
@accountRouter.get("/accounts/{username}", response_model= schemas.Account)
async def get_account(username: str):
    account = AccountModel.getAccountByUsername(username)
    return account

# Update an existing account
@accountRouter.put("/accounts/{username}", response_model= schemas.Account)
async def update_account(username: str, account_update: schemas.AccountUpdate):
    AccountModel.updateAccount(username, update_account)

# Delete an account by username
@accountRouter.delete("/accounts/{username}", response_model=Dict[str, str])
async def delete_account(username: str):
    AccountModel.deleteAccount(username)
