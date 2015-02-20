# README

## malriq, Maltego RiskIQ transforms

Make RiskIQ API calls to generate new nodes.

## Installation

#### Install dependencies

````bash
sudo python setup.py install
./generate_mtz.sh
````

#### Set up credentials
* Open ~/.canari/malriq.conf
* Input token and private key from creds from RiskIQ API token/key generated through web UI

#### Install transforms
* Open Maltego
* Click main icon at top left, with 3 circles
* Go to Import->Import Configuration
* Select malriq.mtz (within the same directory as this README)
* Click Next
* Select Transforms + Transform Sets
* Click Next, then Finish

#### Try it
* Right click any Domain, IP or URL
* Select Run Transform->RiskIQ-> Any available imported transform
* If no results are generated, no results found in API response
