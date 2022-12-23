import os 
data_validation_dir = os.path.join("a","data_validation")
report_file_path = os.path.join(data_validation_dir,"report.yaml")
print(report_file_path)
# def write_yaml_file(file_path,data:dict):
#     try:
#         file_dir=os.path.dirname(file_path)
#         os.makedirs(file_dir,exist_ok=True)
#         with open(file_dir,"w") as file_writer:
#             yaml.dump(data,file_writer)
#     except Exception as e:
#         raise SensorException(e, sys)
file_dir=os.path.dirname(report_file_path)
os.makedirs(file_dir,exist_ok=True)
with open(f"{file_dir}/report.yaml","w") as f:
    f.write("a")
# with open(file_dir)as f:
#     f.write("ss")