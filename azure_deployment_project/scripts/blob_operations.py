from azure.storage.blob import BlobServiceClient
import os

# I initialize the connection string for both storage accounts
conn_str_a = 'Storage_Account_A_Connection_String'
conn_str_b = 'Storage_Account_B_Connection_String'

# I initialize BlobServiceClient for both storage accounts to access to the service
blob_service_a = BlobServiceClient.from_connection_string(conn_str_a)
blob_service_b = BlobServiceClient.from_connection_string(conn_str_b)

# Define the container a
container_a = 'container-a'
container_b = 'container-b'

# to Upload 100 blobs to Storage Account A 
# i need to get the container client with the blob service client
# and then upload to the container the blobs
container_client_a = blob_service_a.get_container_client(container_a)
for i in range(1, 101):
    blob_name = f"blob_{i}.txt"
    blob_client_a = container_client_a.get_blob_client(blob_name)
    blob_client_a.upload_blob(f"This is blob number {i}", overwrite=True)

# i copy blobs from Storage Account A to Storage Account B
container_client_b = blob_service_b.get_container_client(container_b)
for i in range(1, 101):
    blob_name = f"blob_{i}.txt"
    blob_client_a = container_client_a.get_blob_client(blob_name)
    blob_client_b = container_client_b.get_blob_client(blob_name)
    
    # Start the copy operation
    blob_client_b.start_copy_from_url(blob_client_a.url)

print("Blobs uploaded and copied successfully.")
