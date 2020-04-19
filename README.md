# covid_19_api_django

## Description
This is an implementation of an API which provides covid-19 data from the Johns Hopkins University. It regularely fetches the official data in csv format.
The app is running on Kubernetes. The API lives in its own pod and a Kubernetes cronjob is deployed regularely to fetch new data.

## Execute
1. Create Kubernetes secret for the postgres database. It should be created in dev_ops/postgres
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: postgres-credentials
type: Opaque
data:
  user: username
  password: password
```

2. Create all Kubernetes ressources in the dev_ops folder
```bash
kubectl apply -f dev_ops
```
