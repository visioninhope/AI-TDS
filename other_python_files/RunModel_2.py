import pefile as pe
import datetime
import time
import joblib
import warnings
import numpy as np
import os


def tds_cal(z):
    time_now = datetime.datetime.now()
    chk = time_now.year

    file_time = z.FILE_HEADER.TimeDateStamp
    file_time_readable = int(time.strftime('%Y', time.gmtime(file_time)))

    if 1980 <= file_time <= chk:
        return 1
    else:
        return 0


def predict_2(s):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    remo = list(current_dir.rsplit("\\"))
    remo = remo[:len(remo) - 1]
    ram_maha = "\\".join(remo)

    third_model_path = os.path.join(ram_maha, 'Modals_proj\\third_model.pkl')
    third_column_names_path = os.path.join(ram_maha, 'Modals_proj\\third_column_names.pkl')

    xy = joblib.load(third_column_names_path)
    warnings.filterwarnings("ignore")

    my_model = joblib.load(third_model_path)
    feats = []

    engdict = {}

    try:

        z = pe.PE(s)

        engdict.update({"checksum": z.OPTIONAL_HEADER.CheckSum})
        engdict.update({"ohs": (z.OPTIONAL_HEADER.SizeOfCode + z.OPTIONAL_HEADER.SizeOfInitializedData)})
        engdict.update({"code size": z.OPTIONAL_HEADER.SizeOfCode})
        engdict.update({"major sub ver": z.OPTIONAL_HEADER.MajorSubsystemVersion})
        engdict.update({"minor sub ver": z.OPTIONAL_HEADER.MinorSubsystemVersion})
        engdict.update({"char": z.FILE_HEADER.Characteristics})
        engdict.update({"major linker ver": z.OPTIONAL_HEADER.MajorLinkerVersion})
        engdict.update({"mach": z.FILE_HEADER.Machine})
        engdict.update({"sub system": z.OPTIONAL_HEADER.Subsystem})
        engdict.update({"major image ver": z.OPTIONAL_HEADER.MajorImageVersion})
        engdict.update({"minor linker ver": z.OPTIONAL_HEADER.MinorLinkerVersion})
        engdict.update({"dll char": z.OPTIONAL_HEADER.DllCharacteristics})
        engdict.update({"size stack res": z.OPTIONAL_HEADER.SizeOfStackReserve})
        engdict.update({"n sec": len(z.sections)})
        engdict.update({"exe hdr adr": z.DOS_HEADER.e_lfanew})
        engdict.update({"addr entry point": z.OPTIONAL_HEADER.AddressOfEntryPoint})
        engdict.update({"sign": z.NT_HEADERS.Signature})
        engdict.update({"tds": tds_cal(z)})
        engdict.update({"major os ver": z.OPTIONAL_HEADER.MajorOperatingSystemVersion})

        for i in z.sections:
            # print(i)

            if str(i.Name.decode()).startswith(".text"):
                engdict.update({"Text_entro ": i.get_entropy()})
                engdict.update({"Text_phys addr": i.Misc_PhysicalAddress})
                engdict.update({"Text_pointerRawData": i.PointerToRawData})
                engdict.update({"c base": (z.OPTIONAL_HEADER.ImageBase + i.VirtualAddress)})
                engdict.update({"Text_byte addr": i.VirtualAddress})
                engdict.update({"Text_sec size": i.SizeOfRawData})
                engdict.update({"Text_ver size": i.Misc_VirtualSize})

            if str(i.Name.decode()).startswith(".data"):
                engdict.update({"Data_sizeRawData": i.SizeOfRawData})
                engdict.update({"Data_entro": i.get_entropy()})
                engdict.update({"Data_pointRawData": i.PointerToRawData})
                engdict.update({"dbase": (z.OPTIONAL_HEADER.ImageBase + i.VirtualAddress)})
                engdict.update({"Data_byte addr": i.VirtualAddress})
                engdict.update({"Data_ver size": i.Misc_VirtualSize})
                engdict.update({"Data_phys addr": i.Misc_PhysicalAddress})
                engdict.update({"Data_char": i.Characteristics})

            if str(i.Name.decode()).startswith(".rsrc"):
                engdict.update({"Rsrc_sizeRawData": i.SizeOfRawData})
                engdict.update({"Rsrc_entro": i.get_entropy()})
                engdict.update({"Rsrc_phys addr": i.Misc_PhysicalAddress})
                engdict.update({"Rsrc_ver size": i.Misc_VirtualSize})

        for i in xy:
            try:
                feats.append(engdict[i])
            except:
                # print(i)
                pass

        probs = my_model.predict_proba(np.array([feats]))

        maino = [my_model.predict(np.array([feats])), probs]

        return "code: success", maino
    except ValueError:
        return ("parse incomplete : absence of vital sections of the pe file, indicating obfuscation and malware "
                "behaviour"), [
            np.array([1]), [0.5, 0.5]]
    except pe.PEFormatError as e:
        return e, []
