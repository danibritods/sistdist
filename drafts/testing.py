print(3*'\n')

Dict_message={ }
Dict_message[id_receiver]={}
id_sender_1 = 'mandante'
id_sender_2 = 'mandante2'
id_receiver = 'recebedor'
message1 = 'OI PRIMO'
message2 = 'OI sobrinho'
index = 1



# SERVER{
#     B:{
#         {
#             "A": "oipudim"
#         }
#     }
#     C:{
#         {"A":["tchaupudim", "oidnv"]
#         "B":["gato"]}
#       }
# }
# B:{
# #         {
# #             "A": "oipudim"
# #         }
# #     }

Dict_message[id_receiver][id_sender] = [message]
index+=1
to_insert = Dict_message[id_receiver][id_sender]
to_insert.append(message)
Dict_message[id_receiver][id_sender] = to_insert


Dict_message[id_receiver][id_sender_2] = [message1]
index+=1
to_insert = Dict_message[id_receiver][id_sender_2]
to_insert.append(message2)
Dict_message[id_receiver][id_sender_2] = to_insert

print(Dict_message)


print(3*'\n')
