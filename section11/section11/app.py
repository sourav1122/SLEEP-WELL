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
    return CRLF.join(lines)
def refresh_token():
    url = "https://oauth2.googleapis.com/token"
    headers = [
             ("grant_type",  "refresh_token"),
             ("client_id", "xxxxxx"),
             ("client_secret", "xxxxxx"),
             ("refresh_token", "xxxxx"),
             ]

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
refresh_token()
    #response = json.decode(response)
#print(refresh_token())
    
