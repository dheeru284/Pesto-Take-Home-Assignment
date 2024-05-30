# Pesto-Take-Home-Assignment
Data Engineering

# AdvertiseX Data Engineering Case Study

This repository contains a data engineering solution for AdvertiseX, a digital advertising technology company. The solution includes data ingestion, processing, storage, and monitoring to handle ad impressions, clicks, conversions, and bid requests.

## Repository Structure

- `data_ingestion/`: Scripts for data ingestion.
- `data_processing/`: Scripts for data processing and correlation.
- `data_storage/`: Scripts for data storage setup and optimization.
- `error_handling/`: Scripts for error handling and monitoring.
- `config/`: Configuration files for the project.

## Getting Started

### Prerequisites

- Python 3.8+
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/advertisex-data-engineering.git
    cd advertisex-data-engineering
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure your environment using `config/config.yaml`.

## Data Ingestion

Scripts for ingesting data from various sources:
- `ingest_ad_impressions.py`
- `ingest_clicks_conversions.py`
- `ingest_bid_requests.py`

## Data Processing

Scripts for processing and correlating the data:
- `process_data.py`
- `correlate_data.py`

## Data Storage

Scripts for setting up and optimizing data storage:
- `storage_setup.py`

## Error Handling and Monitoring

Scripts for error handling and monitoring:
- `monitoring.py`

## Configuration

Configuration files for the project are located in the `config/` directory:
- `config.yaml`: Main configuration file.
- `logging.yaml`: Logging configuration.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

