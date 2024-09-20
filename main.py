from worker import Worker
from tier1 import Tier1
from tier2 import Tier2
from tier3 import Tier3
from entryrecord import EntryRecord

if __name__ == "__main__":
    worker = Worker("Abdullah", "abdullah@example.com", 3000)
    tier1 = Tier1(basic_service=100)
    tier2 = Tier2(extra_service=200)
    tier3 = Tier3(500, name="Abdullah", email="haider@122",salary=5500)
    entry_record = EntryRecord("09:00 AM", "10:00 AM", 500, "2024-01-01", "Sedan", "Model X")

    print(worker.get_detail())
    print(tier1.perform_wash())
    print(tier2.perform_wash())
    print(tier3.perform_wash())
    print(entry_record.get_details())
