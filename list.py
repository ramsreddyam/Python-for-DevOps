my_s3_bucket = ['ramnas_bucket', 'veeras_bucket', 'chethans_bucket']

my_s3_bucket.append("rams_bucket")
print(my_s3_bucket)

my_s3_bucket.remove("chethans_bucket")
print(my_s3_bucket)


is_present = 'veeras_bucket' in my_s3_bucket

print(is_present)

is_present = 'vedas_bucket' in my_s3_bucket

print(is_present)

length = len(my_s3_bucket)

print(length)