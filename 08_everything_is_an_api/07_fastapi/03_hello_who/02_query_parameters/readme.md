# Query Parameters

Query parameters are the name=value strings after the ? in a URL, separated by & characters.

Start Uvicorn with the command line

    uvicorn hello:app --reload

Test in the browser
    
    http://127.0.0.1:8000/hi?who=Shawaal

Test with Requests

    python test_query_param.py