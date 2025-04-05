# ins_mini_proj

VIDEO DEMO GOOGLE DRIVE LINK: https://drive.google.com/file/d/17bXRIDLPXZ_3AkZmlFXPFNFJraDoK7UY/view?usp=sharing

# Digital Signature Standard (DSS)

This project is a simple demonstration of the **Digital Signature Standard (DSS)** implemented using Python and Flask. The web application allows users to **digitally sign messages** and **verify signatures** using a simplified version of the **Digital Signature Algorithm (DSA)**.

## Project Structure

```
.
├── app.py            # Main Flask application
├── dss.py            # Core DSA logic (key generation, signing, verifying)
├── templates/
│   ├── index.html    # Home page with forms for signing and verifying
│   └── result.html   # Results display page
```

## Features

- Message Signing: Generate digital signatures (r, s) for any user-input message.
- Signature Verification: Verify the validity of the message and its digital signature.
- Simplified DSA: Uses fixed cryptographic parameters with SHA-1 hashing.

## How It Works

### 1. Key Generation
- Upon starting, `SimpleDSA` generates:
  - Private key `x`
  - Public key `y = g^x mod p`
  - Fixed parameters `p`, `q`, and `g` as per the DSS standard.

### 2. Signing
- Hash the message using SHA-1.
- Generate a random `k`, compute:
  - `r = (g^k mod p) mod q`
  - `s = k⁻¹(H(m) + x*r) mod q`
- The signature is `(r, s)`.

### 3. Verification
- Recalculate:
  - `w = s⁻¹ mod q`
  - `u1 = H(m)*w mod q`
  - `u2 = r*w mod q`
  - `v = ((g^u1 * y^u2) mod p) mod q`
- Signature is valid if `v == r`.

## Usage

1. Install dependencies:
   ```bash
   pip install flask pycryptodome
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open your browser at `http://127.0.0.1:5000`.

4. Use the interface to sign a message or verify a signature.

## Web Interface

- `index.html`: 
  - Input a message to sign.
  - Input a message with r and s values to verify.

- `result.html`: 
  - Shows the signed values or verification results.

## Conclusion

This project offers a practical and educational example of how the Digital Signature Standard (DSS) operates using a simplified DSA implementation. Through a user-friendly web interface, users can interactively understand the signing and verification process. This tool is valuable for learning purposes and for gaining insights into digital signature mechanisms in cryptographic systems.

