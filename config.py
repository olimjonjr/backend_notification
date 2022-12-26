from firebase_admin import credentials

# cred = credentials.Certificate({
#   "type": "service_account",
#   "project_id": "service-app-6aa56",
#   "private_key_id": "f681322b987c3290fa7e0fc9c44d9fd8a1229086",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8BWq/Zwiwm0+2\nZqIAPsqSA8SAfEeqSyDPZBf1kb974RYLmpQF5EERtPex7Pjl/VRF6trepGGqvzDx\nru68Sjl8yVE11lfweC+SCCj8HqIRRsfs55ZIbxeSem/yvyHfKtQJ31W6L1cubsxO\n2TgHBJnDUShwn+fhnCHV5sOmWf1mJd5/dzzUo8BX5u46hS9YYKTTK/+N/kLmpjFN\n0lQ6JktOoNf+ngAIXiitpQJdSGLSMO+jFlRpLArj4bFcfJd7BmH2lzQz/Rz7PI+S\ndTWLepW+a4GbJ5ImBAmM0zcMw6zDwPl0JQ6JmCtyzDb/5ReXGg1knUGhisiSeCDS\nSkHVGB0zAgMBAAECggEAOd7i9cmVQ6JyHP6m8zNgbyPIuhFGj5QzI5I3y6ZSDSOB\nAQ5RbCTOoFAWgwWgsE1SQHjiZ++pff/95Q2GPp8L5awjGlKAW6vqXGS1lLArCu1B\nwNmhCGdlFnkn9su8da99dxJuFPHYQBrrOIOkOojAeP0EWPHm0aqYQXmXE58UHvmW\n17FxLZaT+HWM+Kb184vy9wkgxtT2Iw7yQGzNJ0cvqINvVKnjE/mUE9oSBnVGq8DL\nMvu+qfUZRjQ3TxIWzXFSs+YPVwHTK0apX+TYYFqq/p8xfEX2jHRy/AMTT4UnpblS\nLpEMvmEm6oW8cGNYBL9wLFKCSzLteHRBCniBfWxmaQKBgQDfcBJDc1Z/8B/1ZnLx\nuqWInMUf+1XayuIS89OzzK5rRUSoIoqzuqO3CbJt1fnPAlrS6/xgQCrtwTzu0jhs\n4bxzonSfLyYD5DPKRpt9ztDyFmVhrPjM1zKCxkfEBtX9xOuyKxnL0vQ3AWUnoU1/\nvI2UsoHKFjr30A4Y5YUS/W+P+QKBgQDXbAlQU7GONujbuZeMJiZLGalYgfDHSsEM\nuaJ3/hYSSOQUZQxnWAtS93w/zum+j8wS9WPvYR8TIX7DK8gjHe9yiUArJfZMCZPR\n0l/Fal9duWvPt10j49AX167y4rEc4i1GHoGvMTAPyK2HPG4mvhH9be2RX9q5fD3o\n//8tAMq5iwKBgQCo60dDawz4CAeBNQStL1g54Zs9xHtxv3QOs/tWsOUj/+gZ3JNT\nsURX+qLEWsJS+ArF7taLxbcuq6pvOsqhtj8MhML6HWD2DC4DPEINaK+adcgLggNO\niVqMd26GCkz5X0h5GBCWgVNTymA5B79ZVKkMw69PomLOOqKNu+dRJfyTsQKBgHy6\nxyHFc9b+IBGpAgBZzm5Ja24dvoYF2IU/rrx/V9Q6dCUC5Q2pQtVFCqH/cgOuSuDn\nSHe/6jgverAS14zNtmjA43CYSGV6XiZtAprRnmosBCp+5uTy8Pf9IATuENLCeqhQ\n3ZHMjyF0dlUJPlYcU1pDnfxAXepr74TLRLqP7NFFAoGAc2o9IKso47Tc8oHpq+uK\nSoLE404K2PQHXnHEVdJMCn72wAm1i+DkCc8wMrx5/QV3JHN+hSs0tWytYB7dc5AB\n8SVNJcF8dQbzB8fqS7+8CBAnJ7dDWQGtU+ZyhpYUma6MmEbylGrb03ajxO4YAb7D\nTb3mIw+BWH4thETfnbX21Fg=\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-bfqj5@service-app-6aa56.iam.gserviceaccount.com",
#   "client_id": "102627170743422874121",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bfqj5%40service-app-6aa56.iam.gserviceaccount.com"
# })


cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "djangofcm-ffc7c",
  "private_key_id": "ff8423ba5c0212f0144bfd569a48ee3617089adf",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDrFWxKQOWJJPUb\nFnIyOkEJIVKn8PZYJk3u6eLnHw4VXWMYHWpqyQ5HSTcW9yErfE6+U/sZ96lDA6En\nYZ37zIIn5y9Hoz24ExuHUxPmC/K7/XKlX9gXiBglwG9SOgOf39qrHfppVax1h7vd\nx3yY6b+eMMdL40cXkIm6kPXjSauu8nAfHflMLOH+feUdPaDUFq5hjzztnTyxSNWz\nYgcLgY7PSlzBdrwrgEI0dc2EGEZKrtJNs0DK1nKlSQyvFy0HhiJWjP52EFa7rLLg\nLhWqLYT8BTECySqW27w8mKsCIh84ZcouZhjMZcs/tD6O9O1IT8bpxIjzQhFIZ9Yw\nZkG0jkfRAgMBAAECggEACBH7CYzdybio6MOmAEnArCQRNtkOU+teDIrJ8n497lzU\n3IyR99WBddAHzJ7c7CW/JvMyG8Dv9hrR9aH5GZ5P2jfVBy64R9vxZigOIafHrvgd\n70XG4NPtZEpivUi8PB5OtEYkr74JsW/gnVX5AIoxvP1WsikSFTct4JI+ZrhDj7oL\nvAtZCWlr2AO0CIWgfanWM1LKsU2OSXrTjKI9vbGnTUCim6c6RKgjlD8zOkOuNwCO\nZNZw5LA3a5oIoa+TnX4H8tc3SsPuL7O5L6dKYehUZR3CsKRXiCibsA/grKnztxGt\nsDYNNpxuuMxYM4XZ5GBHuNCPaTJIIl6Hr95dDadSIwKBgQD8RcxSyYz5Iy4OYEs9\nZbDG8ZTsM3/PvU18nLD1fEwdxl6khTecP6OllJ5mcVByKsq6qP/7SXNnS0QrRwJ0\nMqa447cYfQo1yUHmvGvuJIg1D0qSt7IrcvW/b5fuLqPqCXmiZC9C363ngJtCJkmv\nutEyGEc2QbmtiXHDgI74MwCE/wKBgQDujpvi/vqRcDIdwMJoNxRkR9TDmjUjyNMy\ndndzO7h8XgVk8u4ZUOBllXSBoKT+UYcfNAhlLh7uUaRc/cfrg/Q9039F4K+x0dPk\nRsAVSzFA984xUPI5UqYJxaMj9/dPGu1b3BH/GMZg4pKHVoOYet7tmUQZzyIYnGOz\nGVpb17kjLwKBgBxVtqJh0vy0r9qbhDfsMRPXVJPHIQbzSz3A17tq7520hzLRZ7Kc\nD0Rs0fHNrmx0U/rtOns9/8FNWeXGfwcQHVvM7+bHPJtX9Jf29+Ryo/3ZrtWV3mQ0\n8FdFMHpnMK/7ynar7AcF2qGS911RsZsUT6ThxzXX4gQU2PtNeEF2cQt/AoGANawe\nRJcrlvdQP0N0OfBShTFoHE4gsJlpcwwWWfXQzyJ0Qj8p9MYuhox2tweGt7VuGkYh\nsWoMCYCS410x0rpQhGyGURl5Th+wdca5RtExFrXqTUwyA1WmB8LQrrIGkWS0jJtZ\n7TQMxhWT9CEx4GecqoZ2PPxOZo0hHVWR7+H8RH8CgYBfgnbx2qg02om2ar/0D/5v\nOJImRjhOuzJVbfDGX/DdVRv3uLN2fX9KhrWLrl3zyqJ3CqfDWzmQkT5L63HX/cwr\nkAqQlpe6HZ6o46BXqxJZRTydg+yqVJHV+/140+W6++ZBblxWylrjxz0Famz0CiCl\n7jgrCSQ/E3hnzgNgMEl4iQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-xc6fb@djangofcm-ffc7c.iam.gserviceaccount.com",
  "client_id": "106217869141458747145",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xc6fb%40djangofcm-ffc7c.iam.gserviceaccount.com"
})

