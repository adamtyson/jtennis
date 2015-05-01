using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace JuliaSearleTennis.Controllers
{
    public class CommunityController : Controller
    {
        // GET: Schools
        public ActionResult SchoolsProgramme()
        {
            return View();
        }

        public ActionResult LondonYouthGames()
        {
            return View();
        }
    }
}