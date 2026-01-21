import os
import sys
from pathlib import Path

# Ensure project root is on path
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

# Correct settings module
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "anarchy_and_lace.settings"
)

import django
django.setup()

from django.core import serializers
from django.apps import apps

app_config = apps.get_app_config("catalog")

objects = []
for model in app_config.get_models():
    objects.extend(model.objects.all())

data = serializers.serialize("json", objects, indent=2)

fixtures_dir = BASE_DIR / "catalog" / "fixtures"
fixtures_dir.mkdir(parents=True, exist_ok=True)

fixture_path = fixtures_dir / "catalog.json"
fixture_path.write_text(data, encoding="utf-8")

print(f"Wrote {len(objects)} objects to {fixture_path}")
