from ccdc.io import EntryReader
from ccdc.molecule import Molecule

reader = EntryReader('CSD') # Load the database

# Refcodes

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
    'VENYUI']

# Loop through refcodes

for refcode in refcodes:
    try:
        entry = reader.entry(refcode) # Retrieve the entry by refcode
        smiles = entry.molecule.smiles # Convert to SMILES
        print(f"{refcode}: {smiles}")

    except KeyError:
        print(f"Entry not found for refcode: {refcode}")
        
    except Exception as e:
        print(f"Error processing {refcode}: {str(e)}")
