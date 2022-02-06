import sys
from models import Record
import pandas as pd
from datetime import datetime


try:
	start  = int(sys.argv[1])
	end = int(sys.argv[2])
	shift = int(sys.argv[3])
except IndexError:
	raise ValueError("This function takes 3 positional arguments: start, stop, shift")

datime = datetime.now().strftime("%I-%M-%B-%d-%Y")
writer = pd.ExcelWriter(f"output_data/{start}-{end}.xlsx")


def chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]


def extract(start, end, shift):
	records = Record.query.filter(Record.id >= start, Record.id < end).all()
	records_chunks = list(chunks(records, shift))

	for index, record_list in enumerate(records_chunks):
		names = [record.name for record in record_list]
		emails = [record.email for record in record_list]

		raw_data = {
			"Názov firmy": names,
			"Email": emails	
		}

		df = pd.DataFrame(raw_data)
		print(df)
		df.to_excel(writer, "Sheet" + str(index))		
		writer.save()



if __name__ == "__main__":
	extract(start, end, shift)
