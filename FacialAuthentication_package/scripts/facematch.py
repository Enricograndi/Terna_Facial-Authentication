import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException

apikey =  "e3ba7c2e-026e-45a1-8209-542e16c67580"#'YOUR_API_KEY'

#come gestire apikey a livello globale? 
def match_image(check_image, target_image):   
    # Configure API key authorization: Apikey
    configuration = cloudmersive_image_api_client.Configuration()
    #'YOUR_API_KEY'
    configuration.api_key['Apikey'] = apikey
    # create an instance of the API class
    api_instance = cloudmersive_image_api_client.FaceApi(cloudmersive_image_api_client.ApiClient(configuration))
    try:
        # Compare and match faces
        api_response = api_instance.face_compare(check_image, target_image)
    except ApiException as e:
        #describe the error
        print("Exception when calling FaceApi->face_compare: %s\n" % e)
    
    return api_response