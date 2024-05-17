# ZipAzurePythonFunctions
Workaround to zip up and deploy Azure functions


## How To
- Create your function and ensure it works locally
- build dependencies on local machine
    ```
    pip install  --target="samplefunction/.python_packages/lib/site-packages"  -r requirements.txt
    ```
- Deploy to Azure using azure function tools
    ```
    func azure functionapp publish <FUNCTION_APP_NAME> --no-build --subscription <SUB_ID>
    ```