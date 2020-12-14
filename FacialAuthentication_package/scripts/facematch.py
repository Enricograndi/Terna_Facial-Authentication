import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException

apikey = "e3ba7c2e-026e-45a1-8209-542e16c67580"  # 'YOUR_API_KEY'


def match_image(check_image, target_image):
    """Connect to the cloudmersive host in order to ask to perform the match
    using the 2 image given as parameter. check_image is the image that will
    be machted with target_image.

    :param path: The path of the two images
    :type path: string
    :return: the Json containing infos about the match
    :rtype: Json
    """
    # Configure API key authorization: Apikey
    configuration = cloudmersive_image_api_client.Configuration()
    configuration.api_key['Apikey'] = apikey
    # create an instance of the API class
    instance = cloudmersive_image_api_client.ApiClient(configuration)
    api_instance = cloudmersive_image_api_client.FaceApi(instance)
    try:
        # Compare and match faces
        api_response = api_instance.face_compare(check_image, target_image)
    except ApiException as e:
        # Describe the error
        print("Exception when calling FaceApi->face_compare: %s\n" % e)
    return api_response