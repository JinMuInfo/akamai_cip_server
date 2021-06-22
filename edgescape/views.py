from django.http import HttpResponse
from akadata import EdgeScape

list_keys_return = [
    "country_code",
    "region_code",
    "city",
    "network",
    "company",
    "timezone",
    "default_answer"
]

def return_200(request):
    return HttpResponse(200)

def lookup_ip(request):
    try:
        tmp_ip = request.GET.get("ip")
        if tmp_ip is None:
            result_final = "No paramater \"ip\" provided!"
        else:
            result_final = tmp_ip + ": [ "
            es_client = EdgeScape(host="127.0.0.1", port=2001)
            result_lookup = es_client.ip_lookup(tmp_ip, timeout=200)
            for key_tmp in list_keys_return:
                if key_tmp in result_lookup.keys():
                    if key_tmp == "default_answer":
                        if result_lookup[key_tmp] == True:
                            result_lookup[key_tmp] = "Y"
                        else:
                            result_lookup[key_tmp] = "N"
                    result_final = result_final + key_tmp + ": " +result_lookup[key_tmp]
                    if key_tmp != list_keys_return[-1]:
                        result_final = result_final + ", "
                    else:
                        result_final = result_final + " ]"
                else:
                    continue
    except Exception as identifier:
        result_final = identifier

    return HttpResponse(result_final)
