'''
A code that will create a summary csv for all descriptors.

Made by Leo Arogundade (19/07/2024)
'''

# Import libraries 
import ccdc 
from ccdc import io, descriptors
from ccdc.io import EntryReader
import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors3D, rdMolDescriptors, MolFromMolFile, MolFromSmiles, MolFromSmarts, Fragments
import pandas as pd 
import numpy as np
from os import listdir
import os
import csv

# Function list
def atomnum(mol_ccdc):
    '''
    A function that calculates how many atoms are in the molecule
    
    Input: Molecule generated through ccdc
    Output: The number of atoms
    '''
    
    atomnum = len(mol_ccdc.atoms) # Get the number of atoms
    return atomnum # Return the number of atoms

def bondnum(mol_ccdc):
    '''
    A function that calculates how many bonds there are in the molecule
    
    Input: Molecule generated through ccdc
    Output: The number of bonds
    '''
    
    bondnum = len(mol_ccdc.bonds) # Get the number of bonds
    return bondnum # Return the number of bonds

def heavyatomsnum(mol_ccdc):
    '''
    A function that calculates how many heavy atoms there are in the molecule
    
    Input: Molecule generated through ccdc
    Output: The number of heavy atoms
    '''
    
    heavyatomsnum = len(mol_ccdc.heavy_atoms) # Get the number of heavy atoms
    return heavyatomsnum # Return the number of heavy atoms

def heteroatomsnum(mol_ccdc):
    '''
    A function that calculates how many heteroatoms are in the molecule
    
    Input: Molecule generated through ccdc
    Output: The number of heteroatoms
    '''
    
    heteroatomsnum = 0 # Start a counter for the number of heteroatoms
    for atom in mol_ccdc.atoms: # Loop through each atom in the molecule
        symbol = atom.atomic_symbol  # Get atomic symbol of the atom
        if symbol not in ['C', 'H']: # Check if the atom is a heteroatom (not C or H)
            heteroatomsnum += 1 # Add 1 to the heteroatom counter if it is not a H or C
    return heteroatomsnum # Return the number of heteroatoms

def rotatablebondsnum(mol_ccdc):
    '''
    A function that calculates how many rotatablebonds there are in the molecule
    
    Input: Molecule generated through ccdc
    Output: The number of rotatable bonds
    '''
    
    rotatablebondsnum = 0 # Start a counter for the number of rotatable bonds
    for bond in mol_ccdc.bonds: # Loop through each bond
        if bond.is_rotatable == 'True': # Check if the bond is rotatable
            rotatablebondsnum =+ 1 # Add 1 to the counter if it is rotatable
    return rotatablebondsnum # Return the number of rotatable bonds

def numofrings(mol_ccdc):
    '''
    A function that calculates how many rings are in the molecule
    
    Input: Molecule generated through ccdc
    Output: The number of rings in the molecule
    '''
    
    numofrings = len(mol_ccdc.rings) # Get the number of rings
    return numofrings # Return the number of rings

def aromaticringnum(mol_ccdc):
    '''
    A function that calculates the number of aromatic rings in the molecule
    
    Input: Molecule generated through ccdc
    Output: The number of aromatic rings in the molecule
    '''
    
    rings = mol_ccdc.rings # Get the rings
    aromatic_list = [] # Make a list to put the aromatic rings in

    for ring in rings: # Loop through each ring
        test = ring.is_aromatic # See if the ring is aromatic
        if test == True: # If it is aromatic...
            aromatic_list.append(ring) # Add the ring to the aromatic rings list
    aromaticringnum = len(aromatic_list) # Get the number of aromatic rings
    
    return aromaticringnum # Return the number of aromatic rings

def sp3hybridisedcarbons(mol_rdkit):
    '''
    A function that calculates how many sp3 carbons there are in the molecule
    
    Input: Molecule generated through RDKit
    Output: The number of sp3 carbons there are in the molecule
    '''
    
    sp3carboncount = 0 # Make a counter
    for atom in mol_rdkit.GetAtoms(): # Loop through each atom of the molecule
        if atom.GetSymbol() == 'C':  # Check if the atom is Carbon
            if atom.GetHybridization() == Chem.HybridizationType.SP3: # Check if it is sp3
                sp3carboncount += 1 # Add to counter if it is sp3
    return sp3carboncount # Return the number of sp3

def asphericity(mol_rdkit):
    '''
    A function to calculate asphericity
    
    Input: Molecule generated through RDKit
    Output: Asphericity value
    '''
    
    asphericity = Descriptors3D.Asphericity(mol_rdkit) # Calculate asphericity using RDKit
    return asphericity # Return the calculated asphericity

def eccentricity(mol_rdkit):
    '''
    A function to calculate eccentricity
    
    Input: Molecule generated through RDKit
    Output: Eccentricity value
    '''
    
    eccentricity = Descriptors3D.Eccentricity(mol_rdkit) # Calculate eccentricity using RDKit
    return eccentricity # Return the calculated eccentricity

def internalshapefactor(mol_rdkit):
    '''
    A function to calculate internal shape factor
    
    Input: Molecule generated through RDKit
    Output: Internal shape factor value
    '''
    
    internalshapefactor = Descriptors3D.InertialShapeFactor(mol_rdkit) # Calculate internal shape factor using RDKit
    return internalshapefactor # Return the calculated internal shape factor
    
def normprincmomratio1(mol_rdkit):
    '''
    A function to calculate normalized principal moment ratio 1
    
    Input: Molecule generated through RDKit
    Output: Normal principle moment ratio 1 value
    '''
    
    normprincmomratio1 = Descriptors3D.NPR1(mol_rdkit) # Calculate NPR1 using RDKit
    return normprincmomratio1 # Return the calculated NPR1
    
def normprincmomratio2(mol_rdkit):
    '''
    A function to calculate normalized principal moment ratio 2
    
    Input: Molecule generated through RDKit
    Output: Normal principle moment ratio 2 value
    '''
    
    normprincmomratio2 = Descriptors3D.NPR2(mol_rdkit) # Calculate NPR2 using RDKit
    return normprincmomratio2 # Return the calculated NPR2

def firstprincmomofinertia(mol_rdkit):
    '''
    A function to calculate the first principal moment of inertia
    
    Input: Molecule generated through RDKit
    Output: First priciple moment of inertia value
    '''
    
    firstprincmomofinertia = Descriptors3D.PMI1(mol_rdkit) # Calculate PMI1 using RDKit
    return firstprincmomofinertia # Return the calculated PMI1

def secondprincmomofinertia(mol_rdkit):
    '''
    A function to calculate the second principal moment of inertia
    
    Input: Molecule generated through RDKit
    Output: Second priciple moment of inertia value
    '''
    
    secondprincmomofinertia = Descriptors3D.PMI2(mol_rdkit) # Calculate PMI2 using RDKit
    return secondprincmomofinertia # Return the calculated PMI2

def thirdprincmomofinertia(mol_rdkit):
    '''
    A function to calculate the third principal moment of inertia
    
    Input: Molecule generated through RDKit
    Output: Third priciple moment of inertia value
    '''
    
    thirdprincmomofinertia = Descriptors3D.PMI3(mol_rdkit) # Calculate PMI3 using RDKit
    return thirdprincmomofinertia # Return the calculated PMI3

def radiusofgyration(mol_rdkit): 
    '''
    A function to calculate radius of gyration
    
    Input: Molecule generated through RDKit
    Output: Radius of gyration value
    '''
    
    radiusofgyration = Descriptors3D.RadiusOfGyration(mol_rdkit) # Calculate radius of gyration using RDKit
    return radiusofgyration # Return the calculated radius of gyration

def molsphericityindex(mol_rdkit):
    '''
    A function to calculate molecular sphericity index
    
    Input: Molecule generated through RDKit
    Output: Molecular sphericity index value
    '''
    
    molsphericityindex = Descriptors3D.SpherocityIndex(mol_rdkit) # Calculate sphericity index using RDKit
    return molsphericityindex # Return the calculated sphericity index

def planeofbestfit(mol_rdkit):
    '''
    A function to calculate the plane of best fit
    
    Input: Molecule generated through RDKit
    Output: The plane of best fit
    '''
    
    pbf = rdMolDescriptors.CalcPBF(mol_rdkit) # Calculate the plane of best fit using RDKit
    return pbf # Return the calculated plane of best fit

def topologicalPSA(mol_rdkit):
    '''
    A function to calculate the topological polar surface area
    
    Input: Molecule generated through RDKit
    Output: The TPSA
    '''
    
    psa = rdMolDescriptors.CalcTPSA(mol_rdkit) # Calculate the TPSA using RDKit
    return psa # Return the calculated TPSA

def molecularweight(mol_ccdc): # Define a function to calculate the molecular weight
    '''
    A function to calculate the molecular weight
    
    Input: Molecule generated through ccdc
    Output: Molecular weight
    '''
    
    mw = round(mol_ccdc.molecular_weight, 2) # Round the molecular weight to 2 decimal places
    return mw # Return the rounded molecular weight

def pointgroup(mol_ccdc): # Define a function to determine the point group
    '''
    A function to determine the point group
    
    Input: Molecule generated through ccdc
    Output: Point group
    '''
    
    point_group_mol = descriptors.MolecularDescriptors.point_group_analysis(mol_ccdc) # Perform point group analysis
    pointgroup = point_group_mol[1] # Extract the point group from the analysis
    return pointgroup # Return the point group

def numofoperations(mol_ccdc): # Define a function to get the number of symmetry operations
    '''
    A function to get the number of symmetry operations
    
    Input: Molecule generated through ccdc
    Output: Number of symmetry operations
    '''
    
    point_group_mol = descriptors.MolecularDescriptors.point_group_analysis(mol_ccdc) # Perform point group analysis
    operationsnum = point_group_mol[0] # Extract the number of symmetry operations from the analysis
    return operationsnum # Return the number of symmetry operations

def gcdfile_to_refcode_list(gcd_file_path):
    '''
    A fuction that reads a .gcd file, which should contain only refcodes, and writes them to a list
    
    Input: File path to the .gcd file of interest
    Output: A list of the refcodes returned in the list 'refcode_list'
    '''
    
    refcode_list = [] # Defining the list so it can be called later
    
    with open(gcd_file_path, 'r') as file: # Opening the file that the user has chosen
        for line in file: # Selecting each line in the file
            refcode = line.strip() # Removes any leading or trailing whitespaces
            refcode_list.append(refcode) # Adds the refcode to the list
    print('Refcode list created')
    
    return refcode_list # Returned because we will need it in future functions

def process_molecules(gcd_file_path, csv_newfile_path):
    '''
    A function that reads all the data from multiple csv files and saves it to 1 dataframe so that it can be exported into a single file

    Input: File paths to the gcd folder and where the user want the new csv saved
    Output: A csv file with all the data imported
    '''
    failed_molecule_refcodes_list = []  # List to store refcodes of failed molecules
    database = []  # List to store dictionaries of molecule data
    refcodelist = gcdfile_to_refcode_list(gcd_file_path)
    print(refcodelist)
    for refcode in refcodelist:  # Loop through the refcodes
        print(f'Trying to find the refcode: {refcode} in the .mol folder')
        mol_rdkit = Chem.MolFromMolFile(rf'{refcode}.mol')# Get the molecule from rdkit
        if mol_rdkit is None:  # Check if the molecule generation was successful
            print(f'Failed to load molecule from file: {refcode}')  # Gives error message
            failed_molecule_refcodes_list.append(refcode)  # Stores refcode in failed list
        else:
            csd_reader = EntryReader('CSD')  # Connecting to the CSD database
            mol_ccdc = csd_reader.molecule(refcode)  # Getting the molecule from CSD database

            # Define the descriptors and store them in a dictionary
            descriptors = {
                "Refcode": refcode,
                "Number of atoms": atomnum(mol_ccdc),
                "Number of bonds": bondnum(mol_ccdc),
                "Number of heavy atoms": heavyatomsnum(mol_ccdc),
                "Number of heteroatoms": heteroatomsnum(mol_ccdc),
                "Number of rings": numofrings(mol_ccdc),
                "Number of aromatic rings": aromaticringnum(mol_ccdc),
                "Number of sp3 hybridised carbons": sp3hybridisedcarbons(mol_rdkit),
                "Asphericity": asphericity(mol_rdkit),
                "Eccentricity": eccentricity(mol_rdkit),
                "Internal Shape Factor": internalshapefactor(mol_rdkit),
                "Normalised principle moment ratio 1": normprincmomratio1(mol_rdkit),
                "Normalised principle moment ratio 2": normprincmomratio2(mol_rdkit),
                "First (smallest) principle moment of inertia": firstprincmomofinertia(mol_rdkit),
                "Second principle moment of inertias": secondprincmomofinertia(mol_rdkit),
                "Third (largest) principle moment of inertia": thirdprincmomofinertia(mol_rdkit),
                "Radius of Gyration": radiusofgyration(mol_rdkit),
                "Molecule Sphericity Index": molsphericityindex(mol_rdkit),
                "Plane of best fit": planeofbestfit(mol_rdkit),
                "Topological polar surface area": topologicalPSA(mol_rdkit),
                "Molecular weight": molecularweight(mol_ccdc),
                "Point group": pointgroup(mol_ccdc),
                "Number of operations": numofoperations(mol_ccdc)
            }

            database.append(descriptors)  # Add the dictionary to the database

    # Write the entire database to a CSV file
    csv_newfile_path = os.path.join(csv_newfile_path, 'mol_descriptor_data.csv')
    with open(csv_newfile_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=database[0].keys())
        writer.writeheader()
        writer.writerows(database)
        print(f"Database written to {csv_newfile_path} successfully.")

    print(f'The following refcodes failed to have their molecules generated: {failed_molecule_refcodes_list}')  # Print refcodes that failed to generate molecules

# Example usage:
csv_newfile_path = r'codebase'
process_molecules(r'chiral_refcodes.gcd',
                  csv_newfile_path)
