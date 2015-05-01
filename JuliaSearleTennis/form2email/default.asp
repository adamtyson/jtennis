<html>
<body>
<form action="formmail.asp" method="post">

		<div>
			<!--<input name="_recipients" type="hidden" value="info@\\web-123win\winpackage23\tenniscoaching.london\www.tenniscoaching.london\web\content\form2email\setup_script.cgi" />-->
            <input name="_recipients" type="hidden" value="juliasearle31@gmail.com" />
			<input name="_requiredFields" type="hidden" value="Name,Email,Comments" />
			<input name="_envars" type="hidden" value="HTTP_USER_AGENT,REMOTE_ADDR" />
			<input name="_returnUrl" type="hidden" value="default.asp" />
			<input name="_continueUrl" type="hidden" value="default.asp" />
		</div>

	<table>

		<tr>
			<th align="left">Name:</th>
			<td><input name="Name" type="text" size="50" /></td>
		</tr>
		<tr>
			<th align="left">Email Address:</th>
			<td><input name="Email" type="text" size="50" /></td>
		</tr>

		<tr>
			<th align="left">Comments:</th>
			<td><input name="Comments" type="text" size="50" /></td>
		</tr>
		<tr>
			<th align="left">CAPTCHA Image</th>
			<td><img id="imgCaptcha" src="captcha.asp" /></td>
		</tr>
		<tr>
			<th align="left">Write the characters in the image above</th>
			<td><input name="captchacode" type="text" id="captchacode" size="10" /></td>
		</tr>
	</table>

	<p><input class="button" type="submit" value="Submit" />
	<input class="button" type="reset" value="Clear" /></p>

</form>
<p>To configure this script, please see <a href='http://www.brainjar.com/asp/formmail/'>the documentation</a>.</p>


</body>
</html>
