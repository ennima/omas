#Test API
import api
import db


router.get('/',req,res)
	print("Test de envio por get")
	res.send('enviado por get')

router.post('/jquery',req,res)
	print("Test de envio por post")
	res.send('enviado por post')


