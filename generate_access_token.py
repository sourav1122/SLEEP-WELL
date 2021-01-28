from urllib2 import Request, urlopen, URLError
import json
import mimetools
BOUNDARY = mimetools.choose_boundary()
CRLF = '\r\n'
def EncodeMultiPart(fields, files, file_type='application/xml'):
    """Encodes list of parameters and files for HTTP multipart format.

    Args:
      fields: list of tuples containing name and value of parameters.
      files: list of tuples containing param name, filename, and file contents.
      file_type: string if file type different than application/xml.
    Returns:
      A string to be sent as data for the HTTP post request.
    """
    lines = []
    for (key, value) in fields:
      lines.append('--' + BOUNDARY)
      lines.append('Content-Disposition: form-data; name="%s"' % key)
      lines.append('')  # blank line
      lines.append(value)
    for (key, filename, value) in files:
      lines.append('--' + BOUNDARY)
      lines.append(
          'Content-Disposition: form-data; name="%s"; filename="%s"'
          % (key, filename))
      lines.append('Content-Type: %s' % file_type)
      lines.append('')  # blank line
      lines.append(value)
    lines.append('--' + BOUNDARY + '--')
    lines.append('')  # blank line
    print(CRLF.join(lines))
    return CRLF.join(lines)
def refresh_token():
    #print(val)
    url = "https://oauth2.googleapis.com/token/"
    headers = [
             ("grant_type",  "access_token"),
             ("client_id", "dummy_value.apps.googleusercontent.com"),
             ("client_secret", "dummy_value"),
             ("refresh_token","1//0grv2p2xFhVucCgYIARAAGBASNwF-L9IrlelcE5TTtkyaxnAf1T2UddBCz3egbyGLzPCBlBF1MEd3CgniF6Lauu8jgwLWSsPr0J0"),
             ]
#ya29.a0AfH6SMD9tm8FBT7a7woiFqGb4G4Mn4ZM9gMmGd75YJVSGU9Gyb_dJTUYF9hN3wqkL5FU-6tlos0LGYWaOQ_se9Ub43fT5wWbvy3GaXWsWYFjdjm-50uoECQnu_VHQU6zh7p8huR_MJfohCJCNAJpWriRT8kTcu-XvRk
    files = []
    edata = EncodeMultiPart(headers, files, file_type='text/plain')
    #print(EncodeMultiPart(headers, files, file_type='text/plain'))
    headers = {}
    request = Request(url, headers=headers)
    request.add_data(edata)

    request.add_header('Content-Length', str(len(edata)))
    request.add_header('Content-Type', 'multipart/form-data;boundary=%s' % BOUNDARY)
    response = urlopen(request).read()
    print(response)
l=["1//0grv2p2xFhVucCgYIARAAGBASNwF-L9IrlelcE5TTtkyaxnAf1T2UddBCz3egbyGLzPCBlBF1MEd3CgniF6Lauu8jgwLWSsPr0J0"]
val=l[0]
refresh_token()

    #response = json.decode(response)
#print(refresh_token())
