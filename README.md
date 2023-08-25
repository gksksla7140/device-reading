# device-reading
Brightwheel backend project

## Project Summary

This project implements a web API to receive and process device readings from various devices. The API allows storing and fetching device readings and is built using FastAPI.

## Startup Instructions

To run the web API locally, follow these steps:

1. Clone the repository:
I realized this is a private repo. I can add if you want to clone.
```
git clone https://github.com/gksksla7140/device-reading.git

cd device-readings-web-api
```

2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the FastAPI application using Uvicorn:
```
uvicorn main:app --reload
```

5. The API will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

6. To deactivate the virtual environment:
```
deactivate
```



## API Documentation

### Store Readings

**Endpoint:** `/store_readings/`

**Method:** POST

**Request Body:**
```
json
{ 
    "id": "36d5658a-6908-479e-887e-a949ec199272", 
    "readings": [{ 
        "timestamp": "2021-09-29T16:08:15+01:00", 
        "count": 2 
        }, { 
        "timestamp": "2021-09-29T16:09:15+01:00", 
        "count": 15 
    }] 
}
```
**Response:**
```
{
  "message": "Readings stored successfully"
}
```

### Fetch Readings

**Endpoint:** `/fetch_readings/{device_id}`

**Method:** GET

**Parameters:**
- device_id: The ID of the device to fetch readings for
```
json
{ 
    "readings": [{ 
        "timestamp": "2021-09-29T16:08:15+01:00", 
        "count": 2 
        }, { 
        "timestamp": "2021-09-29T16:09:15+01:00", 
        "count": 15 
    }]
}
```


## Project Reflection

### What roadblocks did you run into when writing your code (i.e., where did you spend the bulk of your time)? 
A significant portion of my effort went into understanding the project's requirements by meticulously reviewing the documentation and defining clear acceptance criteria. Crafting the testing data and composing the test suite also consumed a substantial portion of the development process.

### If you had more time, what part of your project would you refactor? What other tradeoffs did you make?
Given more time, I would refine the testing suite further, ensuring comprehensive coverage across different scenarios. Additionally, I initially considered using heap or priority queues for storing readings, but adapted to using a plain dictionary after realizing that timestamp-based sorting wasn't specified. If possible, I would explore optimizing the handling of duplicate readings while maintaining chronological order by timestamp.