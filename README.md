# NorthArc route planner

Small tools for the NorthArc operations demo: inspect a shipment export and
summarize the deliveries assigned to each route.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py samples/shipments.csv
```

The [operations archive](https://northarc-backups-6c3b6cab.s3.us-east-1.amazonaws.com/index.html)
retains older export configuration and shipment batches. The deployment script
uses the legacy `northarc/deploy/legacy` settings in us-east-1.
