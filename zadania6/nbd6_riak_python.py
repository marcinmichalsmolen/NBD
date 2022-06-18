from riak import RiakClient, RiakNode
from typing import Dict

def addDocument(bucket, key, value):
    document = bucket.new(key, data=value)
    document.store()
    return document

def modifyDocument(document, data: Dict[str, str]):
    document.data[data["key"]] = data['value']
    document.store()
    return document

def deleteDocument(document):
    document.delete()
    return document

if __name__ == "__main__":
  
  # Setup connection, bucket, key and document
  client = RiakClient(nodes=[{'host':'77.55.209.58','http_port':8087}])
  mybucket = client.bucket('s23429')
  documentKey = "testdoc"
  documentValue= {
        'name' : "Test Riak Python" ,
        'value' :  1,
        'valueMultiplier' : 10 ,
        'updatedData' : 20220618
    }
    
  # Add new document
  print('Adding new document...')
  testDocument = addDocument(mybucket, documentKey, documentValue)
  print(f'Added Document: {testDocument.data}\n')

  # Modify newly added document
  print('Modyfing document...')
  testDocumentProperty = {"key": "value", "value": 2}
  testDocument = modifyDocument(testDocument, testDocumentProperty)
  print(f'Updated Document: {testDocument.data}\n')

  # Delete updated document
  print('Deleting document...')
  testDocument = deleteDocument(testDocument)
  print(f'Deleted Document: {testDocument.data}\n')