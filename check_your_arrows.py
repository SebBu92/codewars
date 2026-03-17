def any_arrows(arrows):
    for key in arrows:
        if 'range' in key and 'damaged' not in key:
            return True
        elif 'damaged' in key and 'range' not in key:
            if not key['damaged']:
                return True
        elif 'range' in key and 'damaged' in key:
            if not key['damaged']:
                return True
    return False

#any_arrows([])#, False, "Should handle empty quiver")
#any_arrows([{'range': 5, 'damaged': False}])#, True, "Should handle quiver with undamaged arrows")
#any_arrows([{'range': 5, 'damaged': False}, {'range': 15, 'damaged': True}])#, True,
                   #"Should handle quiver with undamaged arrows")
#any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])#, True,
                   #"Should handle quiver with undamaged arrows")
#any_arrows([{'range': 10, 'damaged': True}, {'damaged': True}])#, False,
                   #"Should handle quiver with damaged arrows")
#any_arrows([{'range': 15, 'damaged': True}, {'range': 40, 'damaged': True}, {'range': 45}, {'damaged': True}])
any_arrows([{'damaged': False}, {'damaged': False}, {'range': 30, 'damaged': True}, {'damaged': True}, {'damaged': False}])