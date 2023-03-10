This is a proof of concept using the DroneBlocks Tello simulator minimal environment with ChatGPT and Python. **Prepare to be amazed!** Steps to get up and running are as follows:

## Get an OpenAI API key

You can crate an OpenAI user account for free. Then go to [this link](https://platform.openai.com/account/api-keys) to create your API key.

## Get a DroneBlocks Simulator key

The steps to get a DroneBlocks simulator key can be [found here](https://pypi.org/project/DroneBlocksTelloSimulator/). This will only work in a Chrome browser for the time being. The simulator lives at the link below:

https://coding-sim.droneblocks.io/

## Clone this repo

```
git clone https://github.com/dbaldwin/DroneBlocks-Tello-Simulator-ChatGPT
```

## Update config.json

You will need to update your config.json file with an OpenAI and DroneBlocks simulator key.

## Create your virtual environment

```
python -m venv venv
```

## Activate your virtual environment:

### Win:

```
.\venv\Scripts\activate
```

### Mac:

```
source venv/bin/activate
```

## Install dependencies:

```
pip install -r requirements.txt
```

## Run the example:

```
python chatgpt_droneblocks_simulator.py
```

## Sample commands

With the DroneBlocks simulator and a ChatGPT prompt open you can try commands like:

```
Please have the drone takeoff, fly up to 50m, do a backflip, and land
```

**Experiment and share some cool examples!**
