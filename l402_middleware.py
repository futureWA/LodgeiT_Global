import os
import yaml
import hashlib
import secrets
import logic # Imports your newly minted Universal Logic Engine

REGISTRY_PATH = r"C:\Users\futur\Documents\LodgeiT_Global\03_Registry\reg-access-control.md"

def load_l402_registry():
    """Reads the L402 pricing and access tiers from the SBRM Registry."""
    if not os.path.exists(REGISTRY_PATH):
        print("[!] Access Control Registry missing. Cannot initialize L402 gateway.")
        return None
        
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        parts = content.split('---')
        if len(parts) >= 3:
            return yaml.safe_load(parts[1])
    return None

def generate_mock_lightning_invoice(amount_sats):
    """
    Simulates a Lightning Node generating an invoice.
    In production, this calls an LND or Core Lightning REST API.
    """
    preimage = secrets.token_hex(32)
    payment_hash = hashlib.sha256(preimage.encode('utf-8')).hexdigest()
    invoice = f"lnbc{amount_sats}n1mockinvoice{secrets.token_hex(16)}"
    return invoice, payment_hash, preimage

def generate_macaroon(tier, caveat):
    """
    Generates a cryptographically signed bearer token (Macaroon) 
    that binds the payment hash to the specific SBRM execution rights.
    """
    # Simplified mock macaroon for architectural demonstration
    raw_token = f"macaroon:{tier}:{caveat}:{secrets.token_hex(8)}"
    return hashlib.sha256(raw_token.encode('utf-8')).hexdigest()

def handle_api_request(tier_name, provided_macaroon=None, provided_preimage=None):
    """
    The main L402 Gateway. Simulates an incoming API request to the global fleet.
    """
    print(f"\n>>> INCOMING REQUEST: API Tier '{tier_name}'")
    registry = load_l402_registry()
    
    if not registry or 'api_tiers' not in registry or tier_name not in registry['api_tiers']:
        print("  [HTTP 404] Requested SBRM service tier not found in registry.")
        return

    tier_data = registry['api_tiers'][tier_name]
    cost = tier_data.get('cost_per_query_sats', 0)
    caveat = tier_data.get('macaroon_caveat', '')

    # 1. Check if this is an unauthenticated initial request
    if not provided_macaroon or not provided_preimage:
        print(f"  [AUTH FAILED] No valid Macaroon or Preimage provided.")
        
        # Generate the Lightning Challenge
        invoice, payment_hash, expected_preimage = generate_mock_lightning_invoice(cost)
        macaroon = generate_macaroon(tier_name, caveat)
        
        print("\n<<< [HTTP 402] PAYMENT REQUIRED")
        print(f"    WWW-Authenticate: L402 macaroon=\"{macaroon}\", invoice=\"{invoice}\"")
        print(f"    Sats Required: {cost}")
        print(f"    Scope Caveat: {caveat}")
        
        # We return the expected preimage here just to simulate the user paying the invoice
        return macaroon, expected_preimage 

    # 2. Check Authentication (Simulating the user returning with proof of payment)
    else:
        print("  [VERIFYING] Client returned with Macaroon and Proof of Payment (Preimage)...")
        
        # In a real system, the Lightning Node validates the preimage against the payment hash.
        # Here we just assume if they have the preimage, they paid the invoice.
        if provided_preimage: 
            print("  [L402 AUTH OK] Lightning settlement confirmed. Cryptographic caveat matches.")
            print("\n  [SYSTEM WAKE] Handing execution over to LodgeiT SBRM Logic Engine...")
            print("="*60)
            
            # Execute the core engine
            logic.run_universal_logic_engine(r"C:\Users\futur\Documents\LodgeiT_Global")
            
            print("="*60)
            print("<<< [HTTP 200] SUCCESS. SBRM Proof Delivered.")
        else:
            print("<<< [HTTP 401] UNAUTHORIZED. Invalid Preimage.")

if __name__ == "__main__":
    print("--- LodgeiT / ClientRelay L402 API Gateway Initialized ---")
    
    # SIMULATION FLOW:
    
    # Step 1: External App (e.g., a custom Stripe integration) requests a complex rollup
    macaroon, expected_preimage = handle_api_request("Complex_Fanout")
    
    # Step 2: The External App pays the Lightning Invoice (Simulated by a pause)
    import time
    print("\n... External Client is paying the Lightning Invoice via their Node ...")
    time.sleep(2)
    
    # Step 3: External App retries the request, attaching the Macaroon and Preimage
    handle_api_request("Complex_Fanout", provided_macaroon=macaroon, provided_preimage=expected_preimage)