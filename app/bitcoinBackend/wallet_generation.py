from bitmerchant.wallet import *
from cryptos import *


class User_Wallet():

    def __init__(self, mnemonic):
        self.__words = mnemonic
        self.__wordsList = mnemonic.split()
        self.__valid_seed = True
        self.__wallet = Wallet.from_master_secret(self.__words)  # generates wallet based on the words
        self.__priv_key = self.__wallet.serialize_b58(private=True)  # generates extended private key
        self.__pub_key = self.__wallet.serialize_b58(private=False)  # generates extended public key

    # compares inputted seed with list of 2048 words
    def __verify_seed(self):
        # word_list = words.split(" ")
        language_List = ["English", "Français", "Español"]
        check_Eng = 1
        check_Fr = 1
        check_Es = 1

        for lang in language_List:

            filename = "bitcoinBackend/locales/{mnemonicLanguage}.txt".format(mnemonicLanguage=str(lang))
            file = open(filename, "r", encoding="utf8")
            file_contents = file.read()
            for word in self.__wordsList:
                if word not in file_contents:

                    if lang == language_List[0]:
                        check_Eng = 0
                    elif lang == language_List[1]:
                        check_Fr = 0
                    else:
                        check_Es = 0

                    file.close()
                    break
            file.close()

            #will return 1 if valid, 0 if not valid

        print(check_Eng, check_Fr, check_Es)
        return check_Eng + check_Fr + check_Es

    # def gen_new_wallet(self, num):
    #     print(entropy_to_words(os.urandom(num)))

    def verifyMnemonic(self):
        return self.__verify_seed()

    # outputs wallet attributes to user.
    # will need authentication from user like password to access
    # will be used strictly for debugging purposes...
    def get_wallet(self):
        if self.__valid_seed:
            print("\nThese words are the mnemonic seed from which "
                  "the public and private extended keys "
                  "are generated \n mnemonic seed: ", self.__words)

            print("\nThis extended private key is used to generate "
                  "derived addresses and public keys which can "
                  "only be accessed by inputting the extended "
                  "private key \n Extended private key: ", self.__priv_key)

            print("\nThe extended public key is visible by all users and "
                  "is derived from the mnemonic seed \nExtended Public Key: ", self.__pub_key)

    # derives a variable amount of address/ public key pairs from extended private
    # key. If a user wants to access their wallet they should input the private key to
    # generate these addresses, after entering their password.
    # using .txt file as simple implementation
    def __gen_derived_address(self, var):
        if self.__valid_seed:
            file = open("derived_addresses.txt", "w")
            file.write("These derived addresses can only be generated by inputting the "
                       "wallets extended private key. If this is lost they cannot be "
                       "regained.\nExtended private key: " + str(self.__priv_key) + "\n\n")
            for x in range(var):
                my_wallet_children = self.__wallet.deserialize(self.__priv_key)
                pub_child = my_wallet_children.get_child(x, is_prime=True, as_private=False)
                # priv_child = my_wallet_children.get_child(x, is_prime=True, as_private=True)
                file.write("public key " + str(x + 1) + ":\t" + str(pub_child.serialize(private=False)) + "\t")

                #dont need to write private keys, unless needed for later on??
                # file.write("private key " + str(x + 1) + ":\t" + str(priv_child.serialize(private=True)) + "\n")
                file.write("address " + str(x + 1) + ":\t" + str(pub_child.to_address()) + "\n")
                # file.write("==========================================================\n")
            file.close()

    def generateWalletContent(self, entry_number):
        self.__gen_derived_address(entry_number)



# wallet1.gen_new_wallet(32)
# wallet1.gen_derived_address(5)
# wallet1.get_wallet()
#
# wallet2 = wallet()
# wallet1.verifyMnemonic(
#     "tip taste bundle desert illness pattern prepare hundred coil dry inhale eternal special off addict there tiger symbol", "English")
# wallet2.get_wallet()

