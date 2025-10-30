from ccdc.io import EntryReader
from ccdc.molecule import Molecule

# Load the database
reader = EntryReader('CSD')

# List of refcodes
refcodes = ['FECKIK',
    'WOCGOK',
    'BOQQUT',
    'BUHMOH',
    'GOCWEA',
    'FOCNIU',
    'NAHFOR',
    'PHTHAO',
    'TOHZUL',
    'ADPRLA',
    'BUKLOK',
    'GILXAD',
    'KEJYOP',
    'TANMAT',
    'BEXGAM',
    'DIHIXL',
    'GILXUX',
    'ZZZRNY',
    'ZUMKUN',
    'BOFWEZ',
    'DIJDAE',
    'BZCOCT',
    'BEVCEK',
    'VIGTUA',
    'VENYUI']  # Add your desired refcodes here

# Loop through refcodes
for refcode in refcodes:
    try:
        # Retrieve the entry by refcode
        entry = reader.entry(refcode)
        
        # Convert to SMILES
        smiles = entry.molecule.smiles
        print(f"{refcode}: {smiles}")
    except KeyError:
        print(f"Entry not found for refcode: {refcode}")
    except Exception as e:
        print(f"Error processing {refcode}: {str(e)}")
