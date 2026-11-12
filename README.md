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

## Development services

The route cache and jump-host addresses are recorded in
[`deploy/services.json`](deploy/services.json). The route cache uses Redis on
TCP 6379. The operations archive remains available independently of the legacy
AWS export job.

A [service directory](docs/index.html) lists the live NorthArc endpoints with connection information and a sitemap.
