using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace JuliaSearleTennis.Controllers
{
    public class TeamController : Controller
    {
        // GET: Team
        public ActionResult OurCoachingTeam()
        {
            return View();
        }
    }
}