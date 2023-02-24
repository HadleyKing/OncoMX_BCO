# OncoMX Conversion

Repo for tracking the conversion of OncoMX BCO db to [2791](https://opensource.ieee.org/2791-object/ieee-2791-schema/-/blob/master/2791object.json) complient objects.

## Steps

1) Download most recent release of DB via URL:  
- GlyGen:  `https://data.glygen.org/ln2releases/<VERSION>/jsondb/bcodb.json`
	- `10:19:21:OncoMX_BCO:curl -o oncomx_bcodb.json 'https://data.oncomx.org/ln2releases/v-1.0.36/jsondb/bcodb.json'`
- OncoMX: `https://data.oncomx.org/ln2releases/<VERSION>/jsondb/bcodb.json`
2) Run script `sort_bocs.py`
3) Run conversion script from the [BCO Tool](https://github.com/biocompute-objects/bcotool/tree/glygen) repo:

	`python3 bcotool/bco_runner.py convert -b /path/to/directory/where/bcos/`
	
	 This will result in a group of converted BCOs that adhear to the IEEE standard.
 4) Run the `dataBCO_move.py` script: 
 	

