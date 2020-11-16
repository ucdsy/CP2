# Check point 2
This is the check point 1 and 2 for the Autophrase project.<br />

Requirements:<br />
Ubuntu:<br />

g++ 4.8 $ sudo apt-get install g++-4.8<br />
Java 8 $ sudo apt-get install openjdk-8-jdk<br />
curl $ sudo apt-get install curl<br />

MacOS:<br />

g++ 6 $ brew install gcc6<br />
Java 8 $ brew update; brew tap caskroom/cask; brew install Caskroom/cask/java<br />

To run the data ingestion, ran command python3 run.py, this will download the DBLP data in to src/data path.<br />

To ruun the data EDA, ran command python3 run.py with eda in the target(argument), this will ouput and save the eda figures.
