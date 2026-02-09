import papermill as pm
from pathlib import Path
from datetime import datetime

# สร้างโฟลเดอร์
Path("notebooks/executed").mkdir(parents=True, exist_ok=True)
Path("reports/figures").mkdir(parents=True, exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)

# สร้าง timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# ใช้ absolute path
base_dir = Path(__file__).parent.resolve()

# รัน nb01
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running nb01...")
pm.execute_notebook(
    input_path='notebooks/nb01-np-analysis.ipynb',
    output_path=f'notebooks/executed/nb01-analysis-{timestamp}.ipynb',
    parameters=dict(
        input_path_nov=str(base_dir / 'data/raw/2019-Nov-sample-10k.csv'),
        output_rfm_csv=str(base_dir / 'data/processed/rfm_results.csv')
    )
)

# รัน nb02 พร้อมส่ง timestamp และ output directory
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running nb02...")
pm.execute_notebook(
    input_path='notebooks/nb02-np-output.ipynb',
    output_path=f'notebooks/executed/nb02-output-{timestamp}.ipynb',
    parameters=dict(
        input_rfm_csv=str(base_dir / 'data/processed/rfm_results.csv'),
        output_timestamp=timestamp,
        output_figures_dir=str(base_dir / 'reports/figures')  # ส่ง output directory
    )
)

print(f"\n✅ Pipeline completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"📁 Notebooks: notebooks/executed/*-{timestamp}.ipynb")
print(f"📁 Figures: reports/figures/*_{timestamp}.png")