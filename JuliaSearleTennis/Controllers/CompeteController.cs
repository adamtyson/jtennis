using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace JuliaSearleTennis.Controllers
{
    public class CompeteController : Controller
    {
        public ActionResult Tournaments()
        {
            return View();
        }

        public ActionResult Leagues()
        {
            return View();
        }

        public ActionResult Matchplay()
        {
            return View();
        }

        public ActionResult Teams()
        {
            return View();
        }
    }
}