# so_data_pipeline

## Overview
* `so_data_pipline` project helps you to construct the database for the stack overflow dataset. 

* You can download the stack overflow dump file from [Stack Exchange Data Dump](https://archive.org/details/stackexchange), which consists of 6 xml files as below.

<img width="1442" height="922" alt="so_data_pipeline" src="https://github.com/user-attachments/assets/0df295d5-9db3-4925-a31e-4c26118d4453" />

* As the size of the dump file is very large, it is not easy to insert the data to the postgresql database. 
* This project provides easy to follow data pipeline to insert the stack overflow dump file to postgresql database.

---

## Repository Structure
```text
.   
├── data_pipeline/      # Script for inserting the stack overflow dump data to postgresql database
├── div_file/           # Script for dividing the stack overflow dump file
├── hf/                 # Script for inserting header and footer for divided xml files
├── sql/                # Script for Structured Query Language to set up the postgresql 
├── requirements.txt    # Python dependencies
└── README.md
```


## Download the StackOverflow Data Dump
* The raw data can be downloaded from the stackoverflow site 
* Please upzip your downloaded file. 
* You will find 6 xml files in the unzipped folder.
    - Badges.xml
    - Comments.xml
    - PostHistory.xml
    - PostLinks.xml
    - Posts.xml
    - Users.xml
    - Votes.xml
---


## Setup the environment 

* Before running the data pipeline, please set up the python environment and install the database(here, we use postgresql)

### 1. Install PostgreSQL
* Please follow the instructions from the official site to install postgresql on your machine: [PostgreSQL Downloads](https://www.postgresql.org/download/)
* After installing postgresql, please create a database for the stack overflow data dump. 
  - You can use the default database 'postgres' or create a new database.
* Please set the database configuration in `data_pipeline/pg_config.py` file.
  - Please modify the following lines in the `pg_config.py` file according to your database configuration.
  ```python
            db_config={
                'dbname'	: 'your_db_name',       #### your db name       
                'user'		: 'your_db_user',       #### your db user name
                'password'	: 'your_db_password',   #### your db password
                'host'		: 'your_db_host',       #### your db host
                'port'		: 'your_db_port'		#### your db port
                }
  ```
### 2. Setup Python Environment
* Please follow the installation guide below to set up the python environment and install the required packages.

**1) Clone the repository:**
   ```bash
   git clone https://github.com/myokyunghan/so_data_pipeline.git
   cd so_data_pipeline
   ```
**2) Construct python virtual environment**
   ```bash
   # in the 'so_data_pipeline' directory
   brew install pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   source ~/.zshrc
   
   pyenv install 3.10.12
   pyenv versions
   ```
**3) Activate the virtual environment**

   ```bash
   # in the 'so_data_pipeline' directory
   pyenv local 3.10.12
   python3 -m venv venv_so_data_pipeline
   source venv_so_data_pipeline/bin/activate
   ```
   
**4) Install dependencies**

   ```bash
   # in the 'so_data_pipeline' directory
   pip install -r requirements.txt
   ```

---


---

## Software and Code Documentation

### System requirements

### Operating system
 * The code has been tested on the following operating systems:
  - Ubuntu 22.04 LTS

### Software dependencies
* Python 3.10.12
* Required Python packages are listed in `requirements.txt`

### Computational Environment
* Large language model inference used to annotate the difficulty of Stack Overflow questions was conducted on a multi-GPU workstation with the following specifications:
  - GPU: NVIDIA RTX A5000 (24 GB VRAM) × 4
  - CUDA version: 12.9
  - NVIDIA driver version: 575.57.08
* Equivalent GPU configurations with comparable memory capacity are sufficient to reproduce the analyses.

---

## Large Language Model Configuration

* Large language models are used to measure task difficulty and related constructs.
  - Model: LLaMA 3.1 70B Instruct
  - Inference framework: ollama
  - Decoding parameters:
    - Temperature: 0.01
    - Maximum number of generated tokens (`num_predict`): 100
    - Context length (`num_ctx`): 4096
    - Stop tokens: `<s>`, `</s>`

No additional decoding or sampling parameters were used.

---

## Installation guide

### Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/myokyunghan/uneven_automation.git
   cd uneven_automation
   ```
2. Construct python virtual environment
   ```bash
   # in the 'uneven_automation' directory
   brew install pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   source ~/.zshrc
   
   pyenv install 3.10.12
   pyenv versions
   ```
3. Activate the virtual environment 
   ```bash
   # in the 'uneven_automation' directory
   pyenv local 3.10.12
   python3 -m venv venv_uneven_automation
   source venv_uneven_automation/bin/activate
   ```
   
4. Install dependencies
   ```bash
   # in the 'uneven_automation' directory
   pip install -r requirements.txt
   ```
   * Installation typically takes approximately 10-15 minutes on a standard desktop comuter, excluding GPU driver and CUDA installation.




* Download the dump file from Stack Overflow
* Install postgresql for your own database 
* Create the tables 
* Install python
* Set the configuration file  
* Insert the dump data with so_data_pipeline project
    * we automatically divide the dump file 
    * and then insert the data to the database 
