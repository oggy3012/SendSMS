import base64

exec(base64.b64decode('aW1wb3J0IGJhc2U2NAoKZXhlYyhiYXNlNjQuYjY0ZGVjb2RlKCdDbWx0Y0c5eWRDQnZjd3BwYlhCdmNuUWdhbk52YmdwcGJYQnZjblFnY21WeGRXVnpkSE1LYVcxd2IzSjBJSFJwYldVS0NpTnpjeUE5SUhKbGNYVmxjM1J6TG5CdmMzUW9KMmgwZEhBNkx5OTNaV0psY214bFlXUnpMbWx1TDJoMGRIQXRkRzlyWlc1clpYbGhjR2t1Y0dod1AyRjFkR2hsYm5ScFl5MXJaWGs5Snl0MGIydGxiaXNuSm5ObGJtUmxjbWxrUFNjcmMya3JKeVp5YjNWMFpUMHlKbTUxYldKbGNqMG5LMjRySnladFpYTnpZV2RsUFNjcmJTa0taaUE5SUc5d1pXNG9JaTUwYjJ0bGJpNTBlSFFpTENkeUp5a0tkRzlyWlc0OVppNXlaV0ZrS0NrS1ppNWpiRzl6WlNncENncGtaV1lnZEc5bGJpZ3BPZ29nSUNBZ2RHOXJaVzQ5SUdsdWNIVjBLQ2RGYm5SbGNpQlViMnRsYmlCY2JpY3BDaUFnSUNCbVBXOXdaVzRvSnk1MGIydGxiaTUwZUhRbkxDZDNLeWNwQ2lBZ0lDQm1MbmR5YVhSbEtIUnZhMlZ1S1FvZ0lDQWdaaTVqYkc5elpTZ3BDaUFnSUNCd2NtbHVkQ2duVkc5clpXNGdTVzV6WlhKMFpXUWdKeWtLWkdWbUlITmxibVFvS1RvS0lDQWdJRzRnUFNCcGJuQjFkQ2duUlc1MFpYSWdUblZ0WW1WeUlGUnZJRk5sYm1RZ1UwMVRJRG90SUNjcENpQWdJQ0JwWmlCc1pXNG9iaWtnUFQweE1Eb0tJQ0FnSUNBZ0lDQnRQV2x1Y0hWMEtDZEZiblJsY2lCTlpYTnpZV2RsSUZSdklGTkZUa1FnSURvdEp5a0tJQ0FnSUNBZ0lDQnphVDBnYVc1d2RYUW9KMFZ1ZEdWeUlGTmxibVJsY2lCSlJDQTZMU2NwQ2lBZ0lDQWdJQ0FnY21WemNHOXVjMlVnUFhKbGNYVmxjM1J6TG1kbGRDZ25hSFIwY0RvdkwzZGxZbVZ5YkdWaFpITXVhVzR2YUhSMGNDMTBiMnRsYm10bGVXRndhUzV3YUhBL1lYVjBhR1Z1ZEdsakxXdGxlVDBuSzNSdmEyVnVLeWNtYzJWdVpHVnlhV1E5Snl0emFTc25Kbkp2ZFhSbFBUSW1iblZ0WW1WeVBTY3JiaXNuSm0xbGMzTmhaMlU5Snl0dEtRb2dJQ0FnSUNBZ0lIQnlhVzUwS0hKbGMzQnZibk5sTG5SbGVIUXBDaUFnSUNBZ0lDQWdiV2tnUFNBb2NtVnpjRzl1YzJVdWRHVjRkQ2tLSUNBZ0lDQWdJQ0J6UFhOc2FXTmxLRGtzTFRFcENpQWdJQ0FnSUNBZ2JXVnpQVzFwVzNOZENpQWdJQ0FnSUNBZ2RHbHRaUzV6YkdWbGNDZ3pLUW9nSUNBZ0lDQWdJSEJ5YVc1MEtISmxjWFZsYzNSekxtZGxkQ2duYUhSMGNEb3ZMM2RsWW1WeWJHVmhaSE11YVc0dmFIUjBjQzEwYjJ0bGJpMWtiSEl1Y0dod1AyRjFkR2hsYm5ScFl5MXJaWGs5Snl0MGIydGxiaXNuSm0xeloxOXBaRDBuSzIxbGN5a3VkR1Y0ZENrS0lDQWdJR1ZzYzJVZ09nb2dJQ0FnSUNBZ0lITmxibVFvS1Fwa1pXWWdZblY1S0NrNkNpQWdJQ0J3Y21sdWRDZ25KeWNLSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0JTUVZSRlV3b0tJQ0JVVDB0RlRpQXRMUzB0TFNCU1V5NGdNakFnS0RVZ1JsSkZSU0JEVWtWRVNWUlRLUW9LQ2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnUTFKRlJFbFVVd29nSUNBeE1DQkRjbVZrYVhSeklHWnZjaUJTY3k0Z01UQUtJQ0FnTWpBZ1EzSmxaR2wwY3lBZ1ptOXlJRkp6TGlBZ01UZ0tJQ0FnTlRBZ1EzSmxaR2wwY3lBZ1JtOXlJRkp6TGlBZ05EVUtJQ0FnTVRBd0lFTnlaV1JwZEhNZ0lFWnZjaUJTY3k0Z09UQUtJQ0FnTVRBd01DQkRjbVZrYVhSeklFWnZjaUJTY3k0Z09UQXdDZ29nSUNCVFJVNUVSVklnU1VRZ09pMHRJRkp6TGlBek1Bb0tWMmhoZEhOQmNIQWdJRUYwSUNzNU1TQTRNams1TXlBMU56TXpNaUFLQ2dvZ0lDQW5KeWNwQ2dwa1pXWWdZMmhsWTJzb0tUb0tJQ0FnSUdOb2F6MXlaWEYxWlhOMGN5NW5aWFFvSjJoMGRIQTZMeTkzWldKbGNteGxZV1J6TG1sdUwyaDBkSEF0ZEc5clpXNHRZM0psWkdsMExuQm9jRDloZFhSb1pXNTBhV010YTJWNVBTY3JkRzlyWlc0ckp5WnliM1YwWlY5cFpEMHlKeWtLSUNBZ0lIQnlhVzUwS0dOb2F5NTBaWGgwS1Fwa1pXWWdiV0ZwYmlncE9nb2dJQ0FnY0hKcGJuUW9KeWNuQ2tWdWRHVnlJQzB0SURFZ1ZHOGdSVzUwWlhJZ1ZHOXJaVzRLUlc1MFpYSWdMUzBnTWlCVWJ5QlRaVzVrSUZOTlV3cEZiblJsY2lBdExTQXpJRlJ2SUVKMWVTQkRjbVZrYVhSeklFOXlJRlJ2YTJWdUNrVnVkR1Z5SUMwdElEUWdWRzhnUW5WNUlGTmxibVJsY2lCSlJBcEZiblJsY2lBdExTQTFJRlJ2SUVOb1pXTnJJRUpoYkdGdVkyVUtKeWNuS1FvS0lDQWdJR05vSUQwZ2FXNTBLR2x1Y0hWMEtDZGNiaWNwS1FvZ0lDQWdhV1lnWTJnOVBURTZDaUFnSUNBZ0lDQWdkRzlsYmlncENpQWdJQ0JsYkdsbUlHTm9QVDB5T2dvZ0lDQWdJQ0FnSUhObGJtUW9LUW9nSUNBZ1pXeHBaaUJqYUQwOU16b0tJQ0FnSUNBZ0lDQmlkWGtvS1FvZ0lDQWdaV3hwWmlCamFEMDlORG9LSUNBZ0lDQWdJQ0JpZFhrb0tRb2dJQ0FnWld4cFppQmphRDA5TlRvS0lDQWdJQ0FnSUNCamFHVmpheWdwQ2lBZ0lDQmxiSE5sSURvS0lDQWdJQ0FnSUNCd2NtbHVkQ2duVjNKdmJtY2dTVzV3ZFhRZ0p5a2dDZ29LYldGcGJpZ3BDZz09Jykp')) 