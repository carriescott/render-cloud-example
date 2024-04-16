python3 app.py
#!/bin/bash

export AUTH0_DOMAIN='carrie-capstone-agency.uk.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='https://capstone-agency/'

export ASSISTANT='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlZCUVRHY2tvUW1TNkpkcDVNUkF5QiJ9.eyJpc3MiOiJodHRwczovL2NhcnJpZS1jYXBzdG9uZS1hZ2VuY3kudWsuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY2MTJlMDE1Y2Q4MDgxZjI5OGZlMTdhZSIsImF1ZCI6Imh0dHBzOi8vY2Fwc3RvbmUtYWdlbmN5LyIsImlhdCI6MTcxMjYwMjY2NywiZXhwIjoxNzEyNjA5ODY3LCJzY29wZSI6IiIsImF6cCI6Ikt2RERhbEVON1hJamdCRDh6TEJZOGhJY1NVVTRqUGhMIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.AdIQRXVoFrdTZCYd-BHBLg5jmSXf-VVNdRoXdQSb453wBET76mRw4QPd93p47E2iKl1QLpQ6NbwTFyrGfWzBEzYpo0fAyOeIRbByuQkY_kb53i1GxVw6gxIxgCyoO3CL7z_ZgRz9qqwq17LBkZuoJcSWjCpyYAka-kHnRN7mVc2-775DhQtPxHmUTCtK3M9RnYPX9f_J2QFbUdx0BsbthU2JiwZwKj8_hdwosDJ5dZgBTpGUM0NAsgs-4Otn06wR7HaWUlU63isVnKELSSzEptw9cXXChIQ8JTh93tXby3CpbrYY4nCaRd7IrsGxJ2gFIwhf-jeTeOG-WpqKs-fztQ'
export DIRECTOR='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlZCUVRHY2tvUW1TNkpkcDVNUkF5QiJ9.eyJpc3MiOiJodHRwczovL2NhcnJpZS1jYXBzdG9uZS1hZ2VuY3kudWsuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY2MTJlMDNiY2Q4MDgxZjI5OGZlMTdiMCIsImF1ZCI6Imh0dHBzOi8vY2Fwc3RvbmUtYWdlbmN5LyIsImlhdCI6MTcxMjYwNDIyMywiZXhwIjoxNzEyNjExNDIzLCJzY29wZSI6IiIsImF6cCI6Ikt2RERhbEVON1hJamdCRDh6TEJZOGhJY1NVVTRqUGhMIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwiZWRpdDphY3RvciIsImVkaXQ6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.C2oDZUyPBCYInjMd_zjPsz54da4FFF7R6mNsFHzl5E9H0NVlSS8bFh-AqgexOEpAx9P8WLEFcR5qv0CZVrnfOr7eXRGOim4-i_emxJi2FcQMHWV1QdV85WelCG7QCidBUWm2AxrDzNqEsjjZZEkKzJNtDZpgk-f5SjS6aCAkPcjof3gK9Wg9rROQA7XJPkM73IeBM02RExwh-UHxp-NU4uiHAs3hne-DVKXTi7fI1pW4CcJSQUkW7Gm4GcbnpSlwzpKFYqXG3zxfojIvdccQgE4yGOdBf1LjZnSKq5q6X2p3N8mxNvsvW6Up5G2O7X1Vfvg4DpN4Y5GGpa7X-ofRCA'
export PRODUCER='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlZCUVRHY2tvUW1TNkpkcDVNUkF5QiJ9.eyJpc3MiOiJodHRwczovL2NhcnJpZS1jYXBzdG9uZS1hZ2VuY3kudWsuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY2MTJlMDYxNmM0NTRiYTQ1MDk3Yzk5NiIsImF1ZCI6Imh0dHBzOi8vY2Fwc3RvbmUtYWdlbmN5LyIsImlhdCI6MTcxMjYwMzczNSwiZXhwIjoxNzEyNjEwOTM1LCJzY29wZSI6IiIsImF6cCI6Ikt2RERhbEVON1hJamdCRDh6TEJZOGhJY1NVVTRqUGhMIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZWRpdDphY3RvciIsImVkaXQ6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.qHRk8wZK1_DZtWmN3u6YRgitp2t5o9pgWuzHai-2sAgid-epOcUVf7fUIW-YIR62rcOcZ2yjanNaSjqU3c75XOjsv-lIjnl9N2JtjaU7Ee4iSyKFC86pLYcAqxTTCQ_TGVthgdMwsY1sj9s-Xf4LhrpxELeoAKZbc5LZGAUqc77367lwZumeHA4SEd-IfEVRc06K4KVl62TIay_Lbfd8MHq7c5EUBDH0VzSWf-8Vn9QoIkL4dBI-3VqRjIeG2MmAkQM-hXCJR-fEkxuv4Mov3mSuEoUx5RKmwAM8yiRdLEBmblD4rEDYNaoPIAFiEWnfWsjVf7emHBMMuTyBvIN8tg'

export DATABASE_URL="postgresql://postgres@localhost:5432/postgres"
export EXCITED="true"

echo "setup.sh script executed successfully!"
